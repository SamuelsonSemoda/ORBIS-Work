#Napište funkci censorship(text, word), která z řetězce text postupně odstraňuje výskyty slova word. Po každé úpravě text vypíše (viz ukázka).

def censorship(text, word):
  print(text)
  while word in text:
    text = text.replace(word, "", 1)
    print(text)
