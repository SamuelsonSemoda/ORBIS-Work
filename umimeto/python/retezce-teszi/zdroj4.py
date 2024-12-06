#Napište funkci zigzag(text), vypíše zadaný text 'cikcak' na dva řádky s prázdnými místy vyznačenými tečkami (viz ukázkový výstup).

def zigzag(text):
    line1 = []
    line2 = []
    
    for i, char in enumerate(text):
        if i % 2 == 0:
            line1.append(char)
            line2.append('.')
        else:
            line1.append('.')
            line2.append(char)
    print("".join(line1))
    print("".join(line2))
