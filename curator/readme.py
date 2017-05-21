import os
from curator.util import markdown
from curator.util import lang_extensions
from curator import settings

CONFIG = settings.load_config()
FOLDER = CONFIG["output_path"]
README_PATH = os.path.join(FOLDER, CONFIG["readme_name"])


def write_readme(submissions):
    with open(README_PATH, 'w+', newline='\n') as f:
        _write_header(f)
        for platform, s in submissions.items():
            _write_platform_submissions(f, s, platform)
        f.close()


def _write_header(file):
    file.write(markdown.h1(CONFIG["readme_title"]))
    file.write(markdown.paragraph(CONFIG["readme_description"]))


def _write_platform_submissions(file, submissions, platform):
    file.write(markdown.h2(platform))
    file.write(markdown.table_header(
        "Problem", "Source", "Language", "Difficulty"))
    for submission in submissions:
        name = submission["name"]
        language = submission["language"]
        difficulty = submission["difficulty"]
        link = submission["link"]
        file_name = name + "." + lang_extensions.extension(language)
        file_path = submission["platform"] + "/" + file_name
        file.write(markdown.table_row(
            markdown.link(name, link),
            markdown.link("Source", file_path), language, difficulty))
