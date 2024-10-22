#Napište funkci stairs_sequence(n), která obsahuje postupně se prodlužující sekvence prvních k čísel, tj. nejdříve je samotná 1, potom 1, 2, potom 1, 2, 3. Posloupnost má délku n.

def stairs_sequence(n):
    num = 1
    limit = 1
    for i in range(n):
    	print(num)
        if num % limit == 0:
            num -= limit
            num += 1
            limit += 1
        else:
            num += 1
