#Upravte funkci stars(n), aby vypisovala n hvězdiček, přičemž každá skupina pěti hvězdiček bude oddělena kolmou čárou.

def stars(n):
    spaces = 5
    for i in range(1, n+1):
        print("*", end="")
        if i % spaces == 0:
            print("|", end="")
    print()
