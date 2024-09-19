#Obr Pažouch má sedmimílové boty. Umí v nich dělat pouze sedmimílové kroky. Chce jít na návštěvu za jednou ze tří obryň (Xaverka, Ygelitka a Zubatka). 
#Obryně bydlí ve vzdálenosti x, y a z mil. Obr potřebuje funkci can_visit(x, y, z), která rozhodne, zda může alespoň jednu z obryň navštívit (tj. vyjde mu to přesně na sedmimílové kroky). 
#Obr už se pokusil funkci napsat, ale úplně se mu to nepovedlo. Opravte ji.

def can_visit(x, y, z):
    return x%7 == 0 or y%7 == 0 or z%7 == 0

#returns True or False
