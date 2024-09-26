#Napište funkci power_test(a, b), která otestuje, zda je jedno z čísel a, b druhou mocninou toho druhého. Pokud žádnou druhou mocninu nenajde, tak funkce alespoň vypíše bagr.

def power_test(a, b):
    if a**2 == b:
    	print(b, "je druhou mocninou", a)
    elif b**2 == a:
            print(a, "je druhou mocninou", b)
    else:
        print("bagr")
