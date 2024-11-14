#Napište funkci count_a(text), která v řetězci text spočítá počet výskytů písmene 'a' (malé i velké písmeno).

def count_a(text):
  return text.count("a") + text.count("A")
