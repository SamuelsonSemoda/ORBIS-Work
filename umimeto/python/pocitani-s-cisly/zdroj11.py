#Napište funkci print_products(n), která vypíše všechny způsoby, jak jde zadané číslo n vyjádřit jako součin dvou přirozených čísel.

def print_products(n):
	a = 0
    while a != n:
        a += 1
        if n % a == 0:
            print(n, "=", a, "*", n // a) 
