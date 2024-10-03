#Napište funkci multiples(n, limit), která vypíše násobky čísla n, které jsou menší než limit.

def multiples(n, limit):
    multiple = n
    
    while multiple < limit:
        print(multiple)
        multiple += n
