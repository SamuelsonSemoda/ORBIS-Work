#Upravte připravenou funkci count_zeros(n) tak, aby vypisovala počet nul v zápisu čísla n. Připravená verze vypisuje jednotlivé cifry.

def count_zeros(n):
    zero_count = 0
    while n > 0:
        if n % 10 == 0:
            zero_count += 1
        n //= 10
    print(zero_count)
