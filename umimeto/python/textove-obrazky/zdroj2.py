#Napište funkci empty_square(n), která vykreslí textový čtverec o velikosti n, který má uprostřed tečky a na kraji mřížky.

def empty_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
