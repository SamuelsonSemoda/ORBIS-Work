#Napište funkci minimum_difference(numbers), která vrátí nejmenší rozdíl dvou čísel ze seznamu numbers.

def minimum_difference(numbers):
    numbers.sort() #tohle mi seřadí seznam vzestupně
    
    min_diff = float('inf') #tady jsem dal tuto funkci, která udělá to, že nevjětší/nejmenší výsledek
    
    for i in range(1, len(numbers)):
    	diff = numbers[i] - numbers[i-1]
        if min_diff > diff:
            min_diff = diff
    return min_diff
