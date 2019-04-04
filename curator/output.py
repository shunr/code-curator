import os

from curator import settings
from curator.util import lang_extensions

CONFIG = settings.load_config()
OUTPUT_PATH = CONFIG["output_path"]


def prep_output():
    if not os.path.exists(OUTPUT_PATH):
        os.mkdir(OUTPUT_PATH)
    elif not os.path.isdir(OUTPUT_PATH):
        # Output path is not a valid directory!
        return


def write_submissions(submissions):
    for platform in submissions:
        for submission in submissions[platform]:
            platform = submission["platform"]
            language = submission["language"]
            name = submission["name"]
            source = submission["source"]
            folder = os.path.join(OUTPUT_PATH, platform)
            path = os.path.join(
                folder, name + "." + lang_extensions.extension(language)
            )
            if not os.path.exists(folder):
                os.mkdir(folder)
            elif not os.path.isdir(folder):
                # Why would this even happen
                continue
            with open(path, "w+", newline="\n") as file:
                file.write(source)
                file.close()
            print("Writing to " + path)
