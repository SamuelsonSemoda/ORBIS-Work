#Napište funkci collatz(n), která pro zadané kladné celé číslo n opakovaně provádí následující operaci. 
#Pokud je n sudé, vydělíme jej dvěma. Pokud je n liché, vynásobíme jej třemi a přičteme jedničku. Tento postup provádíme tak dlouho, dokud nedostaneme číslo 1.

def collatz(n):    
	while n != 1:
    	print(abs(n))
        if n % 2 == 0:
            n //= 2
        elif n % 2 != 0:
            n *= 3
            n += 1
    print(abs(n))
