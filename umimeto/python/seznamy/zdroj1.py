#Napište funkci five_multiples(num_list), která vezme seznam čísel num_list a vrátí seznam těch čísel ze seznamu, která jsou dělitelná pěti (v původním pořadí).

def five_multiples(num_list):
  return [num for num in num_list if num % 5 == 0]
