#Napište funkci factorial(n), která vrátí faktoriál n (součin všech čísel od 1 do n).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
