#Alice a Bob chodí pravidelně navštěvovat babičku. Alice chodí na návštěvu jednou za A dní, Bob chodí na návštěvu jednou za B dní. Pokud by nějaký den měli přijít oba, přijde jen Alice. 
#Napište funkci visits(n, a, b), která pro následujícch n dní vypíše dny, kdy přijde někdo na návštěvu (viz ukázkový výstup).

def visits(n, a, b):
    for i in range(1, n+1):
    	if i % a == 0:
            print(i, "Alice")
        elif i % b == 0:
            print(i, "Bob")
