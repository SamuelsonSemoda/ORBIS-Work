#Čarodějnice Alenka má p princezen a z žab. Postupně po jedné princezny přečarovává princezny na žáby. 
#Skončí, když jí dojdou princezny, nebo když má 10 žab (má malý rybníček a víc se jich tam nevejde). Napište funkci magic(p, z), která zachytí průběh čarování.

def magic(p, z):
    
    while not(p < 0) and z <= 10:
    	print("P = ", p, ", Z = ", z, sep="")
        p -= 1
        z += 1
