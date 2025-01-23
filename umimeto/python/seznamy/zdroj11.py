#Napište funkci balance_check(operations), která dostane seznam operations operací na účtu (připsání peněz / výběr) a zkontroluje, zda je suma na účtu po celou dobu nezáporná.

def balance_check(operations):  
    balance = 0
    for num in operations:
        balance += num
        if balance < 0:
            return False
	  return True
