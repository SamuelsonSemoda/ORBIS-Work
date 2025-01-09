#Upravte funkci cross(n), aby vykreslovala ze znaků '#' kříž šířky n

def cross(n):
    for i in range(3*n):
        for j in range(3*n):
            centerfillhor = n <= i <= n+n-1
            centerfillver = n <= j <= n+n-1
            if i == n or j == n or centerfillhor or centerfillver:
                print("#", end="")
            else:
                print(".", end="")
        print()
