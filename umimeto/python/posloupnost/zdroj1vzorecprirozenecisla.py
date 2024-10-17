#Napište funkci sum_sequence(n), která vypíše posloupnost délky n, která udává postupné součty přirozených čísel. Například na 3. pozici je číslo 6, protože součet prvních tří přirozených čísel je 1+2+3=6.

def sum_sequence(n):
    for i in range(1, n+1):
		total = (i * (i+1)) // 2 #vzorec na postupnou posloupnost přirozených čísel
        print(total)
