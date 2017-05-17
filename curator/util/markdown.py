def tableHeader(*args):
  s = ""
  t = ""
  for a in args:
    s += a + "|"
    t += "---|"
  return s + "\n" + t + "\n"

def tableRow(*args):
  s = ""
  for a in args:
    s += a + "|"
  return s + "\n"

def link(text, url):
  return "[" + text + "](" + url + ")"

def h1(text):
  return "# " + text + "\n"

def h2(text):
  return "## " + text + "\n"

def paragraph(text):
  return text + "\n"

  