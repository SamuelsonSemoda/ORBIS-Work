#Upravte funkci products(n), aby vypisovala tabulku násobilky prvních n čísel (viz ukázkový výstup).

def products(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end=" ")
        print()
