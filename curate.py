#!/usr/bin/env python3

from curator import *
from curator.platforms import *

output.prep_output()

print("Getting submissions...")

submissions = {
    dmoj.platform_name(): dmoj.fetch(),
    codeforces.platform_name(): codeforces.fetch(),
    spoj.platform_name(): spoj.fetch(),
}

print("Writing to folder...")

output.write_submissions(submissions)
readme.write_readme(submissions)
