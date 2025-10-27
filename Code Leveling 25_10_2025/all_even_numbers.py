numbers = list(range(1, 21))
def get_even(input):
	return input % 2 == 0

even_numbers = list(filter(get_even, numbers))
print(even_numbers)