#Napište funkci fence(n, k), která vypíše plot délky n, ve kterém je vždy k příček (#) za sebou a pak následuje díra (.).

def fence(n, k):
    for i in range(n):
        if i % (k + 1) == k:  # tady zjistí, kdy má udělat tečku - v našem případě, pokud iterace je [i=0 k = 4] - 0 % 5 == 0 != k, [i=1 k = 4] - 1 % 5 == 1 != k, [i=2 k = 4] - 2 % 5 == 2 != k, [i=3 k = 4] - 3 % 5 == 3 != k, [i=4 k = 4] - 4 % 5 == 4 = k
            print(".", end="")
        else:
            print("#", end="")
    print()

fence(14, 4)
