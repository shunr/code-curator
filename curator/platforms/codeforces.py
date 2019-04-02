from collections import defaultdict
import mechanicalsoup
import json

from curator import settings

PLATFORM_NAME = "Codeforces"
SUBMISSIONS_URL = "http://codeforces.com/api/user.status?handle="
PROBLEM_URL = "http://codeforces.com/problemset/problem/"

CONFIG = settings.load_config()["platforms"]["codeforces"]
BROWSER = mechanicalsoup.StatefulBrowser()


def fetch():
    submissions = BROWSER.get(SUBMISSIONS_URL + CONFIG["username"])
    if submissions.status_code != 200:
        # Error connecting to codeforces, throw error
        return list()
    candidates = json.loads(submissions.text)["result"]
    return _get_best_submissions(candidates)


def platform_name():
    return PLATFORM_NAME


def _get_source(contest_id, submission_id):
    BROWSER.open(
        "http://codeforces.com/contest/" + contest_id + "/submission/" + submission_id
    )
    page = BROWSER.get_current_page()
    src = page.find("pre", class_="program-source")
    if src:
        return src.text
    else:
        return None


def _get_best_submissions(candidates):
    result = []
    best_submissions = defaultdict(lambda: ({}, 0))
    for v in candidates:
        if v["verdict"] == "OK":
            problem = v["problem"]
            name = str(problem["contestId"]) + str(problem["index"])
            time = v["creationTimeSeconds"]
            current_time = best_submissions[name][1]
            if time > current_time:
                best_submissions[name] = (v, time)
    for problem_name, v in best_submissions.items():
        submission_object = v[0]
        submission_id = str(submission_object["id"])
        problem = defaultdict(int, submission_object["problem"])
        contest_id = str(problem["contestId"])
        source = _get_source(contest_id, submission_id)
        if not source:
            # Could not fetch source, throw warning
            continue
        submission = {
            "name": problem_name,
            "source": source,
            "language": submission_object["programmingLanguage"],
            "platform": PLATFORM_NAME,
            "difficulty": str(problem["points"]),
            "link": PROBLEM_URL + contest_id + "/" + str(problem["index"]),
        }
        result.append(submission)
    result = sorted(result, key=lambda k: k["name"])
    return result
