#Máte připravenou ukázku, která vykreslí jeden rámeček. Upravte tuto funkci tak, aby frames(n) vykreslilo čtvercovou mřížku n krát n tvořenou rámečky.

def frames(n):
  plus = "+-+"
  lines = "| |"
  for i in range(n):
    for j in range(n):
      print(plus, end=" ")
    print()
        
    for h in range(n):
      print(lines, end=" ")
    print()
        
    for _ in range(n):
      print(plus, end=" ")
    print()
