from curator.platforms import *

from curator import *

config = settings.loadConfig()
print("Getting DMOJ submissions...")
submissions = dmoj.fetch()
if submissions:
  print("Writing to folder...")
  output.writeSubmissions(submissions, config["output_path"])
  readme.writeDmoj(submissions)

