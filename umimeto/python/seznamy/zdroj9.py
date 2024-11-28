#Napište funkci check_sudoku(row), která zkontroluje, zda v zadaný řádek čísel row obsahuje každé číslo od 1 do 9 právě jedenkrát (a nic jiného).

def check_sudoku(row):
	return set(row) == set(range(1,10))
