#Napište funkci pyramid(n), která vykreslí textový obrázek pyramidy o výšce n.

def pyramid(n):
	k = 0

	for i in range(1, n+1):
    	for space in range(1, (n-i)+1):
        	print(end="  ") 
    	while k!=(2*i-1):
        	print("# ", end="")
        	k += 1
    	k = 0
    	print()
