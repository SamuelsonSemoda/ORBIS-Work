#Napište funkci plusminus(n), která vypíše plus pro kladná čísla a mínus pro záporná čísla. Pro nulu vypíše text „nic“.
  def plusminus(n):
    if n > 0:
        print("+")
    elif n < 0:
        print("-")
    else:
        print("nic")
