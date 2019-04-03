from collections import defaultdict

import mechanicalsoup
from curator import settings

CONFIG = settings.load_config()["platforms"]["spoj"]

PLATFORM_NAME = "SPOJ"
LOGIN_URL = "https://spoj.com/login"
SUBMISSIONS_URL = "http://www.spoj.com/status/" + CONFIG["username"] + "/signedlist/"
SUBMISSION_SOURCE_URL = "http://www.spoj.com/files/src/plain/"
PROBLEM_URL = "http://spoj.com/problems/"

BROWSER = mechanicalsoup.StatefulBrowser()


def fetch():
    BROWSER.session.headers["Referer"] = LOGIN_URL
    BROWSER.open(LOGIN_URL)
    BROWSER.select_form("form")
    BROWSER["login_user"] = CONFIG["username"]
    BROWSER["password"] = CONFIG["password"]
    auth = BROWSER.submit_selected()
    print("Authenticated")
    submissions = BROWSER.get(SUBMISSIONS_URL)
    if auth.status_code != 200 or submissions.status_code != 200:
        # Error connecting to spoj, throw error
        return list()

    candidates = _parse_submissions(submissions.text)
    return _get_best_submissions(candidates)


def platform_name():
    return PLATFORM_NAME


def _get_source(submission_id):
    resp = BROWSER.get(SUBMISSION_SOURCE_URL + submission_id)
    if resp.status_code == 200:
        return resp.text
    else:
        return None


def _get_best_submissions(candidates):
    result = []
    best_submissions = defaultdict(lambda: (0, 2 ** 32))
    for k, v in candidates.items():
        if v["result"] == "AC":
            pid = v["problem"]
            time = v["time"]
            current_id, current_time = best_submissions[pid]
            if time < current_time:
                best_submissions[pid] = (k, time)

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
            "difficulty": "N/A",
            "link": PROBLEM_URL + problem_id,
        }
        result.append(submission)
    result = sorted(result, key=lambda k: k["name"])
    return result


def _parse_submissions(plaintext):
    plaintext = plaintext.split("\n")
    numsubs = len(plaintext) - 22

    formatted = {}
    submissions = plaintext[9 : 9 + numsubs]

    for sub in submissions:
        separated = sub.strip("|").split("|")
        separated = list(map(str.strip, separated))
        formatted[separated[0]] = {
            "problem": separated[2],
            "result": separated[3],
            "time": float(separated[4]),
            "language": separated[6],
        }
    return formatted
