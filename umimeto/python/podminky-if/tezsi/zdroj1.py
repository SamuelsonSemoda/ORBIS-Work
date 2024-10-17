#Muzeum programování má následující vstupné: dospělí platí 100 Kč, mládež pod 18 let a důchodci nad 70 let mají vstupné poloviční, děti do šesti let mají vstup dokonce zcela zdarma. 
#Napište funkci print_ticket(age), která pro zadaný věk (age) vypíše cenu vstupenky.

def print_ticket(age):
    if 7 <= age < 18 or 70 <= age:
    	print("Cena:", 50)
    elif 18 <= age <= 70:
        print("Cena:", 100)
    else:
        print("Cena:", 0)
