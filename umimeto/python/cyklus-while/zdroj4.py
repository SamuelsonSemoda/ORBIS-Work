#Martin má míň dřeva než kamenů. Každé kolo vytěží 2 dřeva a 1 kámen. Bude těžit tak dlouho, dokud nebude mít stejně dřeva jako kamenů. 
#Napište funkci materials(d, k), která pro zadaný počet dřeva a kamenů vypíše průběh těžby (viz ukázka).

def materials(d, k):
    drevo = d
    kamen = k
    
    while not(d == k):
    	print("D = ", d, ", K = ", k, sep="")
        d += 2
        k += 1
        
    print("D = ", d, ", K = ", k, sep="")
