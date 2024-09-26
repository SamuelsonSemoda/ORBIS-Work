#Napište funkci compare(a, b), která pro dvě zadaná čísl a, b vypíše informaci o tom, zda jsou stejná, nebo je jedno z nich větší (a které to je).

def compare(a, b):
    if a > b:
        print(a, "je vetsi nez", b)
    elif a < b:
        print(b, "je vetsi nez", a)
	else:
        print("stejna")
