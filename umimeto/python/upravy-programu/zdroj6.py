#Napište funkci odd_even(n), která vypíše prvních n přirozených čísel, přičemž lichá a sudá čísla budou vypsána na střídačku ve dvou řádcích (viz ukázkový výstup).

def odd_even(n):
    for i in range(1, n + 1):
        if i % 2 == 1:
            print(i, end=" ")
    print()

    for i in range(1, n + 1):
        if i % 2 == 0:
            print(" " + str(i), end="")
    print()
