#Napište funkci fibonacci(n), která vypíše prvních n členů Fibonacciho posloupnosti (první dva členy jsou 1, každý další je součtem dvou předchozích).

def fibonacci(n):
    a, b = 1, 1
    
    for _ in range(n):
        print(a)
        a, b = b, a + b
