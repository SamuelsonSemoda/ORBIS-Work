#Čarodějnice chce připravit lektvar lásky. Na přípravu potřebuje 5 slz fénixe a roh jednorožce. Pokud nemá roh jednorožce, může použít 3 ocásky fialových prasátek. 
#V tomto případě jí pak stačí pouze 3 slzy fénixe. Napište funkci magic_test(tears, horns, tails), která pro zadaný počet slz (tears), rohů (horns) a ocásků (tails) rozhodne, zda čarodějnice může lektvar připravit.

def magic_test(horns, tears, tails):
  return tears >= 5 and horns >= 1 or tears => 3 and tails => 3
