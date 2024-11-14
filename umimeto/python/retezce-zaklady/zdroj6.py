#Napište funkci frame(text, symbol), která vypíše text v rámečku tvořeném znakem symbol (předpokládejte, že symbol je řetězec tvořený právě jedním znakem).

def frame(text, symbol):
  text_length = len(text)
  top_bottom = symbol * (text_length + 2)
    
  print(top_bottom)
  print(symbol+text+symbol)
  print(top_bottom)
