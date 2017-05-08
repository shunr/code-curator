from collections import defaultdict
import mechanicalsoup
import json

username = ""
password = ""
base_url = "https://dmoj.ca/accounts/login"

def init():
  browser = mechanicalsoup.StatefulBrowser()
  browser.session.headers['Referer'] = base_url
  browser.open(base_url)
  browser.select_form('form')
  browser["username"] = username
  browser["password"] = password
  resp = browser.submit_selected()
  print(resp)

  sub = browser.get("https://dmoj.ca/api/user/submissions/" + username)
  json_data = json.loads(sub.text)

  for k, v in json_data.items():
    if v["result"] == "AC":
      xd = browser.get("https://dmoj.ca/src/" + k + "/raw")
      print(k, v["problem"], v["points"])
  

