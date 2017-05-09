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
    path = os.path.join(output_path, name + "." + lang_extensions.extension(language))
    with open(path, 'w+') as f:
      f.write(source)
      f.close
    print("Writing to " + path)
 
  
    
  