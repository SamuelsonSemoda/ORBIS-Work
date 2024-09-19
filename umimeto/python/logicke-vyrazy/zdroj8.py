#Napište funkci near_fifty(n), která rozhodne, zda zadané číslo n se nachází 'blízko' čísla 50 nebo 150 (je maximálně o 10 větší nebo menší).

def near_fifty(n)
  return 40 <= n <= 60 or 140 <= n <= 160
