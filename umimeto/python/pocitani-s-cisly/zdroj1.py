#Napište funkci powers(base, n), která vypíše prvních n mocnin čísla base.

def powers(base, n):
    rozsah = 0
    mocnina = 1
    while rozsah < n:
    	  mocnitel = base
        rozsah += 1
        mocnitel **= mocnina
        mocnina += 1
        print(mocnitel)
