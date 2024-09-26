#Napište funkci division(a, b), která podělí zadaná čísla, přičemž dělí to větší tím menším. Pokud nelze provést dělení beze zbytku, vypíše „Nejde“. 
#(Nápověda: zbytek po dělení v Pythonu vypočítáme pomocí operátoru %.)

def division(a, b):
    if a > b:
    	if a%b == 0:
        	print (int(a/b))
        else:
            print("Nejde")
    elif a < b:
        if b%a == 0:
         	print (int(b/a))
        else:
            print("Nejde")
