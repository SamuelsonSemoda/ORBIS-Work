#Napište funkci middle_number(a, b, c), která pro zadaná čísla a, b, c vypíše to prostřední z nich (podle velikosti).

def middle_number(a, b, c):
    if b < a < c or c < a < b:
        print(a)
    elif a < b < c or c < b < a:
        print(b)
    elif b < c < a or a < c < b:
        print(c)
