def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b) # b, a % b je euklidův algoritmus
