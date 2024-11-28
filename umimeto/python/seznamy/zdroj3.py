#Napište funkci average(numbers), která vrátí průměr z čísel v seznamu numbers zaokrouhlený na 1 desetinné místo. Zaukrouhlování děláme pomocí funkce round (viz ukázka).

def average(numbers):
  return round(sum(numbers)/len(numbers), 1)
