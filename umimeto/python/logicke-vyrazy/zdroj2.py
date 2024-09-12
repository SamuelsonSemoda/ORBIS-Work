##Money musí být větší nebo rovno ceně, aby si Pepa mohl koupit zmrzlinu
def icecream_test(money, price):
  return price <= money

print(icecream_test(20, 10))
