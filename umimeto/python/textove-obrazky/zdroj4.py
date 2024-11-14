#Napište funkci cross(n), která vykreslí ze znaků '#' velké X o velikosti n.

def bigX(n):
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
