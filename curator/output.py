import os
from curator.util import lang_extensions

def writeSubmissions(submissions, output_path):
  if not os.path.exists(output_path):
    os.mkdir(output_path)
  elif not os.path.isdir(output_path):
    # Output path is not a valid directory!
    return
  for submission in submissions:
    platform = submission["platform"]
    language = submission["language"]
    name = submission["name"]
    source = submission["source"]
    folder = os.path.join(output_path, platform)
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
 
  
    
  