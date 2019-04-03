import json
from collections import defaultdict

import mechanicalsoup
from curator import settings

PLATFORM_NAME = "DMOJ"
LOGIN_URL = "https://dmoj.ca/accounts/login"
SUBMISSIONS_URL = "https://dmoj.ca/api/user/submissions/"
PROBLEM_URL = "https://dmoj.ca/problem/"

CONFIG = settings.load_config()["platforms"]["dmoj"]
BROWSER = mechanicalsoup.StatefulBrowser()


def fetch():
    BROWSER.session.headers["Referer"] = LOGIN_URL
    BROWSER.open(LOGIN_URL)
    BROWSER.select_form("form")
    BROWSER["username"] = CONFIG["username"]
    BROWSER["password"] = CONFIG["password"]
    auth = BROWSER.submit_selected()
    submissions = BROWSER.get(SUBMISSIONS_URL + CONFIG["username"])

    if auth.status_code != 200 or submissions.status_code != 200:
        # Error connecting to dmoj, throw error
        return list()

    candidates = json.loads(submissions.text)
    return _get_best_submissions(candidates)


def platform_name():
    return PLATFORM_NAME


def _get_source(submission_id):
    resp = BROWSER.get("https://dmoj.ca/src/" + submission_id + "/raw")
    if resp.status_code == 200:
        return resp.text
    else:
        return None


def _get_best_submissions(candidates):
    result = []
    best_submissions = defaultdict(lambda: (0, 0, 2 ** 32))
    for k, v in candidates.items():
        if v["result"] == "AC":
            pid = v["problem"]
            points = v["points"]
            time = v["time"]
            current_id, current_points, current_time = best_submissions[pid]
            if points > current_points or (
                time < current_time and points == current_points
            ):
                best_submissions[pid] = (k, points, time)
    for problem_id, v in best_submissions.items():
        submission_id = str(v[0])
        source = _get_source(submission_id)
        if not source:
            # Could not fetch source, throw warning
            continue
        submission = {
            "name": problem_id,
            "source": source,
            "language": candidates[submission_id]["language"],
            "platform": PLATFORM_NAME,
            "difficulty": str(candidates[submission_id]["points"]),
            "link": PROBLEM_URL + problem_id,
        }
        result.append(submission)
    result = sorted(result, key=lambda k: k["name"])
    return result
