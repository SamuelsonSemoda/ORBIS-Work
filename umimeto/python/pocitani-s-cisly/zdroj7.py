#Kája má rád seznamy čísel. Kája má ale alergii na čísla, která končí na pětku. 
#Napište pro Káju funkci alergy_list(a, b), která vypíše čísla od a po b (včetně), přičemž vynechá čísla, která končí na pětku.

def alergy_list(a, b):
    for i in range(a,b+1):
        if i % 10 != 5:
            print(i, end=" ")      
    print()
