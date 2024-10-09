#Napište funkci zigzag(n), která k zadanému číslu n postupně na střídačku přičítá a odčítá rostoucí mocniny dvojky. 
#Funkce skončí, když takto číslo klesne pod 1 nebo přesáhne 1000. 
#Například k číslu 10, postupně přičítáme 1, odečítáme 2, přičítáme 4, odečítáme 8. 
#Tím dostáváme 10, 11, 9, 13, 5, ...

def zigzag(n):
    power = 0
    while True:
        print(n)
        change = 2 ** power
        n += change
        power += 1
        print(n)
        change = 2 ** power
        n -= change
        power += 1
        
        if not(n > 1 and n < 1000):
            break
            
    print(n)
