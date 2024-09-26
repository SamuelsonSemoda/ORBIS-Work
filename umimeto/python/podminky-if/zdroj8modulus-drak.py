#Drak je naštvaný. Místo princezen mu na oběd přinesli prasata. Navíc pokud prasata nepůjde rozdělit spravedlivě mezi dračí hlavy, tak se hlavy vzájemně pobijí. 
#Napište funkci dragon_test(heads, pigs), která pro zadaný počet dračích hlav (heads) a prasat (pigs), rozhodne, zda bude bitka (prasata nejdou spravedlivě rozdělit), nebo nebude bitka (prasata jdou spravedlivě rozdělit).

def dragon_test(heads, pigs):
    if pigs%heads == 0:
    	print("Nebude bitka.")
    else:
        print("Bude bitka.")
