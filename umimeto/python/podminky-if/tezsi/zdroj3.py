#Napište funkci person_info(name, height, money), která která vypíše informaci o tom, zda kluk jménem name je malý (height je menší než 150) či velký a chudý (money je méně než 1000) nebo bohatý. 
#Výpis pište bez háčků a čárek, viz ukázkový výstup.

def person_info(name, height, money):
	maly = "je maly"
    velky = "je velky"
    chudy = "a chudy."
    bohaty = "a bohaty."
    
    if height < 150 and money < 1000:
        print(name, maly, chudy)
    elif height >= 150 and money < 1000:
        print(name, velky, chudy)
    elif height < 150 and money >= 1000:
        print(name, maly, bohaty)
    else: 
        print (name, velky, bohaty)
