#Napište funkci powers(n, a, b), která vypíše mocniny čísla n, které spadají do intervalu od a do b.

def powers(n, a, b):
    power = 0
    integer = n ** power
    while b >= integer:
		  if a <= integer <= b:
        print(integer)

      power += 1
      integer = n ** power
