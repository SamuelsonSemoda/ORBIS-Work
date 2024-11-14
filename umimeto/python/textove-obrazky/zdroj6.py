#Napište funkci chessboard(n), která vykreslí textovou šachovnici o straně délky n. Políčka šachovnice nechť jsou tvořena znaky '.' a '#'.

def chessboard(n):
  for i in range(n):
    for j in range(n):
      if (i + j) % 2 != 0:
        print(".", end=" ")
      else:
        print("#", end=" ")
    print()
