#Napište funkci make_fancy(text, n), která vypíše text šikmo a navíc n-krát za sebou (viz ukázka).

def make_fancy(text, n):
  for i, char in enumerate(text):
    print(" " * i + (char + " ") * n)
