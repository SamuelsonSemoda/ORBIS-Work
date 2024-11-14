#Napište funkci palindrom(text), která otestuje, zda je zadaný řetězec text palindromem (čte se stejně od začátku jako od konce).

def palindrom(text):
	return text == text[::-1] #[::-1] otočí string
