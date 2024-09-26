#Napište funkci multiples(k, n), která vypíše prvních n násobků čísla k.

def multiples(k, n): # je číslo, které bude mít násobky, n je počet násobkových čísel
    for i in range(1, n + 1): #1 je začátek od prvního násobkového čísla, n + 1 zahrnujeme proto, že chceme aby poslední násobkové číslo bylo zahrnuto
        print(k * i) #k * i = k je určité číslo a i je interace - jak dosáhneme násobku? Interace je řetězec číslic který vždy pokračuje, tím že i vynásobíme k uděláme následující, k=3 k*i -- 3*0 - 3*1 - 3*2 - 3*3 ... 
