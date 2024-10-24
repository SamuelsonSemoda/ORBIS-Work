#Upravte funkci sequences(n), aby vypisovala postupně se prodlužující posloupnosti prvních n čísel (viz ukázkový výstup).

def sequences(n):
    for i in range(n):
        for _ in range(1, i+2): #zde mám proměnnou pro iteraci jinou, pro lepší přehlednost
            print(i, end=" ")
        print()
