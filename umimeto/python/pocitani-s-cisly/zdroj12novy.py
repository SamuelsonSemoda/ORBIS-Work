#Napište funkci print_squares(start, end), která vypíše všechny čtverce (druhé mocniny přirozených čísel) v intervalu od start po end (včetně).

def print_squares(start, end):
    i = 1
    while i * i <= end:
        if i * i >= start:
            print(i * i)
        i += 1
