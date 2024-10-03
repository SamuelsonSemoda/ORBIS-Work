#Pepa má zásobu a avokád a b brambor. Každý den sní 2 avokáda a 3 brambory. Pokud má jednoho z toho nedostatek, je to KRIZE. 
#Pokud má nedostatek obojího, je to KATASTROFA. Napište funkci reserves(n, a, b), která vypíše Pepovi vyhlídky na nejbližších n dní (viz ukázkový výstup).

def reserves(n, a, b):
   	for i in range(1, n+1):
		a -= 2
        b -= 3
		
        if a >= 0 and b >= 0:
            print (i, "OK")
        elif a < 0 and b < 0:
            print (i, "KATASTROFA")
        else:
            print (i, "KRIZE")
