#Napište funkci decide(symbol1, symbol2), která rozhodne, kdo vyhrál ve hře kámen-nůžky-papír. 
#Tahy jsou zadány prvními písmeny (symbol1, symbol2). Funkce má za úkol vypsat písmeno odpovídající tahu, který vítězí, nebo text 'Remiza'.

def decide(symbol1, symbol2):
    kamen = "K"
    papir = "P"
    nuzky = "N"
    
    if symbol1 == kamen and symbol2 == papir or symbol1 == papir and symbol2 == kamen:
        print(papir)
    elif symbol1 == kamen and symbol2 == nuzky or symbol1 == nuzky and symbol2 == kamen:
        print(kamen)
    elif symbol1 == papir and symbol2 == nuzky or symbol1 == nuzky and symbol2 == papir:
        print(nuzky)
    else:
        print("Remiza")
