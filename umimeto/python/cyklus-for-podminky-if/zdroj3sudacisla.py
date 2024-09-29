#Napište funkci zigzag(n), která vypíše čísla od 1 do n do výpisu pod sebe, přičemž sudá čísla odsadí.

def zigzag(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(" ", i)
        else:
    		print(i)

zigzag(8)

#output=
#  1
#    2
#  3 
#    4
#  5
#    6
#  7
#    8
