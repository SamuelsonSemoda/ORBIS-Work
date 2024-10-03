#Napište funkci repeated_division(n), která opakovaně vypisuje a dělí zadané kladné číslo n na poloviny, dokud je větší než nula (viz ukázka). 
#Použijte celočíselné dělení, které v Pythonu zapisujeme pomocí dvou lomítek (//).

def repeated_division(n):
    while n > 0:
    	print(n)
        n //= 2
