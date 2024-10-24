#Napište funkci divisors_count(n), která pro zadané přirozené číslo n vrátí počet jeho přirozených dělitelů.

def divisors_count(n):
	count = 0
	for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
