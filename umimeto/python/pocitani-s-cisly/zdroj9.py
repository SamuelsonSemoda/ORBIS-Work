#Napište funkci numbers_around(n, k), která vypíše seřazeně k menších a větších čísel než n. Místo čísla n vypíše hvězdičku.

def numbers_around(n, k):
    for i in range(n - k, n + k + 1): #od n-k to začíná a od n + k + 1 to končí, tedy vlastně děláme kolik čísel vrátí program od daného čísla.
        if i == n:
            print('*', end=' ')
        else:
            print(i, end=' ')
    print()
