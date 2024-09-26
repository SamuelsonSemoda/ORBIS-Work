#Napište funkci reverse_numbers(n), která vypíše čísla od 1 do n pozpátku.

def reverse_numbers(n):
    for i in reversed(range(1, n+1)): #1 je starting point, n+1 je v jakém range - v mém případě nechci nulu
        print(i)

  #výsledek print(6) = 6,5,4,3,2,1
