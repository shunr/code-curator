from curator.platforms import dmoj

from curator import output
from curator import settings

config = settings.loadConfig()
print("Getting DMOJ submissions...")
submissions = dmoj.fetch()
if submissions:
  print("Writing to folder...")
  output.writeSubmissions(submissions, config["output_path"])

