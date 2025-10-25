from functools import reduce

numbers = [3, 7, 56, 2, 9, 1]

def maximum_value(input, inputs):
	return max(input, inputs)

maximum = reduce(maximum_value, numbers)
print(maximum)