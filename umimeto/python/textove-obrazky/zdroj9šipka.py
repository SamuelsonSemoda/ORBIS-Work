#Napište funkci arrow(n), která vykreslí textový obrázek šipky ze znaků '*' uvnitř čtverce velikosti n tvořeného znaky tečkami. Můžete předpokládat, že n je liché.

def arrow(n):
  half = n // 2
  for i in range(n):
    for j in range(n):
      c = '.'
      if i == j - half or i == half or n-j-1 == i - half:
        c = '*'
      print(c, end="")
    print()
