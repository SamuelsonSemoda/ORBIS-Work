#Napište funkci size_info(n, k), která vypíše pro všechna čísla od 1 do n velmi užitečnou informaci o tom, zda je menší, rovno, nebo větší než k.

def size_info(n, k):
    for i in range(1, n+1):
        if i > k:
        	print(i, ">", k)
        elif i == k:
        	print(i, "=", k)
        else:
            print(i, "<", k)

size_info(5, 3)

#output = 1 < 3
#         2 < 3
#         3 = 3
#         4 > 3
#         5 > 3
