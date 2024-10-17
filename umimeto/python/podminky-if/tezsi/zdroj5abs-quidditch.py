#Intergalaktický famfrpál má složitá pravidla vyhodnocování vítěze. Pokud jeden z týmů má na konci hry alespoň o 50 bodů více, stává se vítězem. 
#Pokud je však rozdíl menší jak 50 bodů, vítězí ten, kdo má méně bodů. Pokud mají týmy bodů stejně, vítězí oba. Napište funkci winner(a, b), která určí, který z týmů A, B je vítězem.

def winner(a, b):
    if a < b and (b-a) > 50:
    	print("B")
    elif b < a and (a-b) > 50:
        print("A")
    elif a > b and abs(a-b) < 50:
        print("B")
    elif a < b and abs(a-b) < 50:
        print("A")
    elif a == b:
        print("AB")
