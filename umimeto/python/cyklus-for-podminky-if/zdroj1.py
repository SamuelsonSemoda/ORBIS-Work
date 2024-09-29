#Pepa označuje čísla dělitelná třemi slovem foo. Ostatní čísla označuje slovem bar. 
#Napište funkci foobar3(n), která vypíše prvních n přirozených čísel společně s jejich označením.

def foobar3(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(i, "foo")
        else:
            print(i, "bar")
