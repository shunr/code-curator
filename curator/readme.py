import os
from curator.util import *
from curator import settings

config = settings.loadConfig()
FOLDER = config["output_path"]
README_PATH = os.path.join(FOLDER, config["readme_name"])

def writeReadme(submissions):
  with open(README_PATH, 'w+') as f:
    _writeHeader(f)
    for platform, s in submissions.items():
      _writePlatformSubmissions(f, s, platform)
    f.close()

def _writeHeader(f):
  f.write(markdown.h1(config["readme_title"]))
  f.write(markdown.paragraph(config["readme_description"]))
      
def _writePlatformSubmissions(f, submissions, platform):
  f.write(markdown.h2(platform))
  f.write(markdown.tableHeader("Problem", "Source", "Language", "Difficulty"))
  for s in submissions:
    name = s["name"]
    language = s["language"]
    difficulty = s["difficulty"]
    file_path = os.path.join(s["platform"], name + "." + lang_extensions.extension(language))
    f.write(markdown.tableRow(s["name"], markdown.link("Source", file_path), language, difficulty))
    
