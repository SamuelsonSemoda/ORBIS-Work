#Kovář má okovat několik koní a potřebuje zjistit, jestli má správný počet podkov. 
#Napište funkci check(p, k), která pro zadaný počet podkov p a počet koní k vypíše, kolik podkov chybí, přebývá, nebo zda je počet správně (formát výstupu viz ukázkový soubor).

def check(p, k):
    kopyta = k * 4
    
    if kopyta % p == 0:
        print("OK")
    elif kopyta % p != 0 and p > kopyta:
        print("Prebyva:", p - kopyta)
    else:
        print("Chybi:", kopyta - p)
