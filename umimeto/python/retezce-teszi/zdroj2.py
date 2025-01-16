#Napište funkci common_prefix(text1, text2), která vrátí společný začátek řetězců text1 a text2.

def common_prefix(text1, text2):
    myText = str()
    for pismeno in range(min(len(text1), len(text2))):
        if text1[pismeno] == text2[pismeno]:
            myText += (text1[pismeno])
    return myText
