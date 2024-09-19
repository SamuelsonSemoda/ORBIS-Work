#Napište funkci big_even(a, b), která vrátí True právě tehdy, když větší z čísel a, b je sudé.

def big_even(a, b):
    return a % 2 == 0 and a > b or b % 2 == 0 and b > a
