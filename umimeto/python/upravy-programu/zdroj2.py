#Napište funkci print_sums(n), která vypíše všechny způsoby, jak jde zadané číslo n vyjádřit jako součet dvou přirozených čísel.

def print_sums(n):
    for i in range(1, n):
        print(n, "=", i, "+", n - i)
