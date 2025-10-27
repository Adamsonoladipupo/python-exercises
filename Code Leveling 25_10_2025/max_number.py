from functools import reduce
numbers = [3, 5, 9, 2, 8]
def get_max(input, inputs):
	return max(input, inputs)
check = reduce(get_max, numbers)
print(check)