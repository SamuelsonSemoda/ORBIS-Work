#Napište funkci every_second_number(num_list), která ze zadaného seznamu čísel num_list vypíše každé druhé číslo (počínaje prvním).

def every_second_number(num_list):
  for i in num_list[::2]:
    print(i)
