##Zadaná hodnota age odpovídá věku teenagera, tj. je mezi 13 a 19 (včetně). Místo or je potřeba použít jinou logickou spojku.
def teenager(age)
	return age > 12 and age <= 19
	
print(teenager(10))
print(teenager(15))
print(teenager(19))
print(teenager(30))
