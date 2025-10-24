from functools import reduce
numbers = [2, 3, 4]

def multiples_of_numbers(number, numbers):
	return number * numbers

multiples = reduce(multiples_of_numbers, numbers)
print(multiples)