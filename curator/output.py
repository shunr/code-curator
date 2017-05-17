import os
from curator.util import lang_extensions
from curator import settings

config = settings.loadConfig()
OUTPUT_PATH = config["output_path"]

def prepOutput():
  if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)
  elif not os.path.isdir(OUTPUT_PATH):
    # Output path is not a valid directory!
    return

def writeSubmissions(submissions):
  for submission in submissions:
    platform = submission["platform"]
    language = submission["language"]
    name = submission["name"]
    source = submission["source"]
    folder = os.path.join(OUTPUT_PATH, platform)
    path = os.path.join(folder, name + "." + lang_extensions.extension(language))
    if not os.path.exists(folder):
      os.mkdir(folder)
    elif not os.path.isdir(folder):
      # Why would this even happen
      continue
    with open(path, 'w+') as f:
      f.write(source)
      f.close
    print("Writing to " + path)
 
  
    