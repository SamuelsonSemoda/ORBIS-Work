#Napište funkci join(text1, text2), která vrátí spojení těchto dvou řetězců, přičemž ten kratší z nich bude první.

def join(text1, text2):
  if len(text1) > len(text2):
    return text2 + text1
  else:
    return text1 + text2
