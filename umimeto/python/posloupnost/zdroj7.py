#Napište funkci repetition_sequence(n), která vypíše posloupnost přirozených čísel, ve které je počet opakování každého čísla roven tomuto číslo. Posloupnost má mít délku n.

def repetition_sequence(n):
    num = 1
    rep = 1

    for i in range(n):
        print(abs(num))
        if num - rep == 0:
            num += 1
            rep = 1
        else:
            rep += 1
