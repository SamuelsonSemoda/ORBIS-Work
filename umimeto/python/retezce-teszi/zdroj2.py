#Napište funkci common_prefix(text1, text2), která vrátí společný začátek řetězců text1 a text2.

def common_prefix(text1, text2):
    prefix = ""
    for char in range(min(len(text1), len(text2))):
        if text1[char] == text2[char]:
            prefix += text1[char]
        else:
            break
    return prefix
