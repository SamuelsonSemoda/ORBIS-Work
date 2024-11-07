#Napište funkci numbers_around(n, k), která vypíše seřazeně k menších a větších čísel než n. Místo čísla n vypíše hvězdičku.

def numbers_around(n, k):
    for i in range(n - k, n + k + 1):
        if i == n:
            print('*', end=' ')
        else:
            print(i, end=' ')
    print()
