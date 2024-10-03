#Magráta má dýně. Navíc má kouzelnou hůlku, se kterou se učí čím dál lépe zacházet. Při prvním mávnutí vyčaruje jednu dýni, při druhém dvě, při třetím tři a tak dále. 
#Jakmile však má Magráta víc jak 20 dýní, přijde Pepan a 10 jich ukradne. Napište funkci magic(k, n), která pro počáteční počet dýní k vypíše vývoj počtu dýní délky n.

def magic(k, n):
    dyne = k
    for i in range(n):
    	dyne += i
        
        if dyne > 20:
            dyne -= 10
            
        print(dyne)           
