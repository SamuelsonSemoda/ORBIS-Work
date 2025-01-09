#Napište funkci bigN(n), která vypíše textový obrázek velkého písmene N na n řádků.

def bigN(n):
  for i in range(n):
    print("|" + " " * i + "\\" + " " * (n - i - 1) + "|")
