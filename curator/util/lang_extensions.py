from curator import settings
translations = settings.loadExtensions()

def extension(lang):
  name = lang.lower()
  if name in translations.keys():
    return translations[name]
  else:
    return name