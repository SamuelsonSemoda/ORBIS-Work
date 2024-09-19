#Napište funkci animals(n), která vypíše n sobů a následně dvakrát tolik losů.

def animals(n):
    for animals in range(n):
    	print("sob")
    for animals in range(n * 2):
        print("los")
       
animals(2)
