from functools import reduce

numbers = [1, 2, 3]

def sum_of_squares_of_numbers(input, inputs):
	return input + inputs**2

square_sum = reduce(sum_of_squares_of_numbers, numbers)
print(square_sum)