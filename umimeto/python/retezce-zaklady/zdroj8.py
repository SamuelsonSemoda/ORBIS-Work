#Napište funkci censorship(text), která vrátí zadaný řetězec text, ve kterém nahradí každé druhé písmeno za X.

def censorship(text):
  censored_text = str()
  for i, char in enumerate(text):
    if i % 2 == 1:
      censored_text += "X"
    else:
      censored_text += char
  return censored_text
