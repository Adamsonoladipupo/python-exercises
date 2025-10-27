from functools import reduce
numbers =  [1, 2, 3, 4]
def get_product_of_square(input, inputs):
	inputs = inputs**2
	return input + inputs

new_list = reduce(get_product_of_square, numbers)
print(new_list)