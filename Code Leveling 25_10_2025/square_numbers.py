numbers = list(range(1, 10))

def square_numbers(input):
	return input**2

new_list = list(map(square_numbers, numbers))
print(new_list)