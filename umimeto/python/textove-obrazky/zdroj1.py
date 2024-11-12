#Napište funkci square(n), která vykreslí čtverec ze znaků mřížky o velikosti n.

def square(n):
    for i in range(n):
    	print("#", end=" ")
        for i in range(n-1):
        	print("#", end=" ")
        print()
