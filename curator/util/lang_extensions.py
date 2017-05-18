from curator import settings
TRANSLATIONS = settings.load_extensions()


def extension(lang):
    name = lang.lower()
    if name in TRANSLATIONS.keys():
        return TRANSLATIONS[name]
    else:
        return name
