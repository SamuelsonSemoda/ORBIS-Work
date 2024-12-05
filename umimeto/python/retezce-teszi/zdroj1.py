#Pan Kaplan (z knížky Pan Kaplan má třídu rád) se rád podepisuje jako K*A*P*L*A*N. 
#Napište funkci add_stars(name), která pro zadané jednoslovné jméno name vrátí podpis v této podobě, tj. velkými písmeny a prokládané hvězdičkami.

def add_stars(name):
  return "*".join(name.upper())
