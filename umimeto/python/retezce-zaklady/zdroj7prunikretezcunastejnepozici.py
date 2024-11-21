#Napište funkci string_intersection(left, right), která pro dva zadané řetězce left a right vypíše písmena, která jsou v obou řetězcích na stejné pozici.

def string_intersection(left, right):
  for char in range(min(len(left), len(right))):
    if left[char] == right[char]:
      print(left[char])
