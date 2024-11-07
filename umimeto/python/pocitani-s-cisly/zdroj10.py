#Napište funkci sum_info(n), která vypíše součet řady prvních n přirozených čísel (viz ukázkový výstup).

def sum_info(n):
    vysledek = 1
    for i in range(1, n+1):
        if i < n:
        	print(i, end="+")
          vysledek += i+1
        elif i == n:
          print(i, end="=")
          print(vysledek)
