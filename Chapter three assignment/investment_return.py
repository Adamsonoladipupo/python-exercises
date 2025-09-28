AMOUNT = 1000
NUMBER_OF_YEARS = 10

for count in range(3):
	investment_return = AMOUNT*(1 + 0.07)**NUMBER_OF_YEARS
	print(f"Investment return of $1000 at 7% after {NUMBER_OF_YEARS} is {investment_return}")
	NUMBER_OF_YEARS += 10 

