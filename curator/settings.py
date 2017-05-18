import json


def load_config():
    return _load("config.json")


def load_extensions():
    return _load("extensions.json")


def _load(file_path):
    with open(file_path) as json_data_file:
        data = json.load(json_data_file)
    return data
