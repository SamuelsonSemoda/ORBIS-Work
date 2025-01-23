#Napište funkci pairs_sum(numbers, x), která vypíše všechny způsoby, jak lze číslo x vyjádřit jako součet dvou čísel ze seznamu numbers. 
#Můžete předpokládat, že seznam numbers obsahuje kladná celá čísla a že se v něm žádné číslo neopakuje. Výpis musí být seřazený podle prvního sčítance (viz ukázkový výstup).

def pairs_sum(numbers, x):
    numbers.sort()
  
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == x:
        print("{} + {} = {}".format(numbers[i], numbers[j], x))
