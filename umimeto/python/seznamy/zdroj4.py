#Napište funkci nonzero_product(numbers), která pro zadaný seznam čísel numbers vrátí součin všech nenulových čísel v seznamu.

def nonzero_product(numbers):
	multiply = 1

  for val in numbers:
    if val != 0:
      multiply = multiply * val
  return multiply
