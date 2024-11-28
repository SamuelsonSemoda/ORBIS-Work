#Napište funkci unique(mylist), která vrátí seznam obsahující každý prvek ze seznamu mylist právě jedenkrát (v pořadí prvních výskytů v původním seznamu).

def unique(mylist):
  seen = set()
  res = []
  for item in mylist:
    if item not in seen:
      res.append(item)
      seen.add(item)
  return res
