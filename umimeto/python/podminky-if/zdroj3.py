#Juraj chce prodat vajíčka a cibule. Na trhu dostane za vajíčko 3 groše a za cibuli 2 groše. 
#V hospodě dostane za vajíčko 5 grošů, ale za cibuli jen jeden. Napište funkci decide(v, c), která pro zadaný počet vajíček v a cibulí c rozhodne, kde je prodej výhodnější. 
#Pokud to vyjde na stejno, půjde Juraj raději na trh, protože to je blíž. Máte připravený program, stačí ho mírně upravit.

def decide(v, c):
    zisktrh = 3*v + 2*c
    ziskhospoda = 5*v + c
    
    if zisktrh > ziskhospoda:
        print("trh")
    elif ziskhospoda > zisktrh:
        print("hospoda")
    else:
        print("trh")
