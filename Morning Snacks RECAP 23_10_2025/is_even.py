numbers = [1,2,3,4,5,6]

def is_even(numbers):
	return numbers % 2 == 0

Even = list(filter(is_even, numbers))

print(Even)