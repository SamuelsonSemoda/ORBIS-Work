#Napište funkci sequence(n, k), která opakovaně obsahuje čísla od 1 do k. Posloupnost má délku n.

def sequence(n, k):
    num = 1
    
    for i in range(1, n+1):
        print(num)
        num += 1
        if i % k == 0:
            num -= k
