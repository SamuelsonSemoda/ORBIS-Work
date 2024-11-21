#Napište funkci first_letters(text), která vypíše první písmena slov ze zadaného řetězce text.

def first_letters(text):
  words = text.split() #text mi to rozdělí na jednotlivá písmena, ale je to uložené do proměnné sloučeně jako  celé slovo
    for chars in words: #cyklus mi iteruje v proměnné words, iterace je tedy chars
      print(chars[0], end=" ")  #jednotlivé chars slova jsou písmena, takže si vyberu pozici, pokud chci první písmeno, dávám chars[0]
    print()
