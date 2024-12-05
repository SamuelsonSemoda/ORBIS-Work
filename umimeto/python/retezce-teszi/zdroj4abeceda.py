#Napište funkci alphabet(n), která vypíše prvních n písmen anglické abecedy. Pokud je n větší jak 26, písmena jsou vypisována opakovaně.

def alphabet(n):
  abeceda = [chr(i) for i in range(65, 91)] #definovaná abeceda, vytahnutá z chr tabulky | pozice 65 a 91 jsou velká písmena
	for i in range(n):
    print(abeceda[i%26])
