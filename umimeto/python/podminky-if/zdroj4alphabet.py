#Napište funkci letters(a, b), která vypíše zadaná dvě písmena a udělá mezi nimi šipku podle toho, jak jsou za sebou v abecedě (viz ukázky).

def letters(a, b):
    if a < b:
    	print(a, "->", b)
	else:
        print(a, "<-", b)

#letters("A", "A")
#letters("X", "P")
#letters("K", "S")
#letters("Z", "Y")
