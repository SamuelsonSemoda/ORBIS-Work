def bigT(n):
    for i in range(n):
        for j in range(n):
            if i == 0:
                print("#", end="")
            if i != 0 and j == 3:
                print("#", end="") 
            elif j / 2 + 1 and i != 0:
                print(" ", end="")
    	  print()
