#Napište funkci helke(text), která vypíše zadaný text, ve kterém ovšem všechny samohlásky nahradí za písmeno e. Můžete předpokládat, že text obsahuje pouze malá písmena anglické abecedy.

def helke(text):
  text = text.replace("o", "e")
  text = text.replace("u", "e")
  text = text.replace("a", "e")
  text = text.replace("i", "e")
  text = text.replace("e", "e")
  text = text.replace("y", "e")
  print(text)
