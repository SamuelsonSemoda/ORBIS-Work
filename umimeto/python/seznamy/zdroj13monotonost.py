#Napište funkci monotonic(numbers), která vrátí True, pokud je seznam čísel numbers rostoucí nebo klesající.

def monotonic(numbers):
    increasing = decreasing = True
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            decreasing = False
        elif numbers[i] < numbers[i-1]:
            increasing = False
	return increasing or decreasing
