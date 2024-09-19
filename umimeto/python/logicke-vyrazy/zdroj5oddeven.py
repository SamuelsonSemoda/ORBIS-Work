#Checks if a is even and b is odd or a is odd and b is even // Returns true if it's pretty pair of odd and even

def nice(a, b):
  return a % 2 == 0 and b % 2 != 0 or a % 2 != 0 and b % 2 == 0
