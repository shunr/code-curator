import os
from curator.util import *
import curator.platforms as pt
from curator import settings

config = settings.loadConfig()
FOLDER = config["output_path"]
README_PATH = os.path.join(FOLDER, config["readme_name"])

def writeDmoj(submissions):
  with open(README_PATH, 'w+') as f:
    f.write("##" + pt.dmoj.platformName() + "\n")
    f.write(markdown.tableHeader("Problem", "Source", "Language", "Points"))
    for s in submissions:
      name = s["name"]
      language = s["language"]
      difficulty = s["difficulty"]
      file_path = os.path.join(s["platform"], name + "." + lang_extensions.extension(language))
      f.write(markdown.tableRow(s["name"], markdown.link("Source", file_path), language, difficulty))
    f.close