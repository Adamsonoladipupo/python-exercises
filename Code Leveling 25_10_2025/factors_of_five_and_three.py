numbers = list(range(1, 51))

def factors_of_five_three(input):
	return input % 5 == 0 and input % 3 == 0

factors = list(filter(factors_of_five_three, numbers))
print(factors)