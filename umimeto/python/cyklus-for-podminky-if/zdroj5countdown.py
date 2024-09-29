#Napište funkci countdown(start, n), která vypíše odpočet o n řádcích, přičemž začíná od čísla start. Jakmile odpočet klesne na nulu, tak už se nevypisují čísla, ale jen BUM.

def countdown(start, n):
    for i in range(start, start - n, -1):
        if i <= 0:
           	print("BUM")
        else:
            print(i)

countdown(6, 10)

#ocekavany vystup dle countdown(6, 10)
6
5
4
3
2
1
BUM
BUM
BUM
BUM
