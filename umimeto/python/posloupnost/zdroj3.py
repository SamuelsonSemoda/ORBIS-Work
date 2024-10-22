#Podle ukázkového výstupu odhalte princip posloupnosti. Napište funkci sequence(n), která vypíše prvních n členů.

def sequence(n):
	
    current = 1
    increment = 1
    
    for i in range(n):
        print(current)
        current += increment
        increment += 1
