from functools import reduce
numbers = list(range(1, 51))
def summation(input, inputs):
	return input + inputs

new_list = reduce(summation, numbers)
print(new_list)