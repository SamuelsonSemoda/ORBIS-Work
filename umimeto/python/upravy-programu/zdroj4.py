#Napište funkci big_five(n), která vykreslí pomocí znaku '#' velkou digitální pětku o šířce n (viz ukázkový výstup).

def big_five(n):
    print("#"*n)
    for i in range(n-2):
        print("#")
    print("#"*n)
    for i in range(n-2):
        print(" "*(n-1) + "#")
    print("#"*n)
