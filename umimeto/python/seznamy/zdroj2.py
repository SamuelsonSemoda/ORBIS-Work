#Napište funkci compute_tax(money_list), která pro zadaný seznam finančních částek vypočítá celkovou daň. 
#Bohatí (200 a víc peněz) platí daň 20. Ti, co nejsou bohatí, ale mají alespoň 100 peněz, platí daň 10. Ostatní daň neplatí. Máte nachystaný základ funkce, který je potřeba opravit a dodělat.

def compute_tax(money_list):
  tax = 0
  for money in money_list:
    if money >= 100 and not(money >= 200):
      tax += 10
    elif money >= 200:
      tax += 20
    else:
      tax += 0
  return tax
