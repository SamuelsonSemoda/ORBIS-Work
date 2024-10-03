#Zahradník Jura získal dvě speciální semínka fazolí. Rostou z nich fazole, jejichž růst se vzájemně ovlivňuje. Ta menší z nich vyroste na dvojnásobek, ta větší z nich se o 1 cm zmenší. 
#Pokud dosáhnou přesně stejné výšky, vyčkávají a nerostou. Napište funkci beans(x, y, n), která pro délky fazolí x a y vypíše prvních n délek podle uvedeného pravidla růstu.

def beans(x, y, n):
    for i in range(n):
        print(x, y)
        
        if x > y:
	    y *= 2
            x -= 1
        elif x < y:
            y -= 1
            x *= 2
