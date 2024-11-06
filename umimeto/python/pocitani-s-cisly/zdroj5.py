#Napište funkci digit_sum(n), která vrátí ciferný součet čísla n.

def digit_sum(n):
  result = 0
	while n > 0:
		  result += n % 10 #přičte poslední číslo/zbytek k result, např. 125 % 10 je 12 a zbytek 5.
		  n = n // 10 #odstraní poslední cifru např. 125 // 10 je 12 místo 12,5. (Vydělí a dostaneme celé čislo)
    return result
