from functools import reduce

numbers = [1, 2, 3, 4, 5]

def sum_of_numbers(input, inputs):
	return input + inputs

summation = reduce(sum_of_numbers, numbers)
print(summation)