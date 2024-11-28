#Napište funkci small_numbers(numbers, k), která vrátí počet čísel menších než k v seznamu numbers.

def small_numbers(numbers, k):
  count = 0
  for i in numbers:
    if i < k:
      count += 1
  return count
