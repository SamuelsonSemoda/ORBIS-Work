#Napište funkci even_numbers(n), která vypíše n sudých čísel (počínaje dvojkou).

def even_numbers(n):
    for i in range(1, n+1): # 1 = o 1 číslo od nuly (kdyby místo 1 byla 0, začíná to vždy od nuly, kdyby -1 tak to začíná od prvníhé záporného čísla od nuly) v našem příp. to začíná od 2
        print(i * 2) # even_numbers(6) -- 2,4,6,8,10,12

  
