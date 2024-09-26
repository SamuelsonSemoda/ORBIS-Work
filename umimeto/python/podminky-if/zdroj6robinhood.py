#Napište funkci robin_hood(money), která chudým (mají méně než 100 peněz) dává (vypíše 'Dar' a zdvojnásobí množství peněz) a bohatým bere (vypíše 'Lup' a odebere 50 peněz). 
#Funkce také vypíše konečný stav peněz. Máte nachystaný základ funkce, který je potřeba opravit a dokončit.

def robin_hood(money):
    if money > 100:
        print("Lup")
		money = money - 50
    else:
        print("Dar")
        money = money * 2
    print("Konecny stav:", money)
