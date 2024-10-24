#Napište funkci divisors(n), která vypíše popořadě všechny přirozená čísla, která dělí n.

def divisors(n):
    div = 0
    while div <= n:
        div += 1
        if n % div == 0:
            print(div)
