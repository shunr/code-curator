from curator import settings

TRANSLATIONS = settings.load_extensions()
EXACT = TRANSLATIONS["exact"]
FUZZY = TRANSLATIONS["fuzzy"]


def extension(lang):
    name = lang.lower()
    if name in EXACT.keys():
        return EXACT[name]
    for key in FUZZY:
        if key in name:
            return FUZZY[key]
    return name
