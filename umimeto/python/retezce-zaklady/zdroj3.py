#Napište funkci duplication(text), která pro zadaný řetězec vrátí řetězec, ve kterém je každé písmeno duplikováno.

def duplication(text):
  a = text
  b = str()
  for char in a:
    b += char + char
  return b
