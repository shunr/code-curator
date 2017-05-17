from curator.platforms import *

from curator import *

config = settings.loadConfig()
output.prepOutput()

print("Getting submissions...")

submissions = {
  dmoj.platformName(): dmoj.fetch()
}

print("Writing to folder...")

for platform, items in submissions.items():
  output.writeSubmissions(items)
  
readme.writeReadme(submissions)

