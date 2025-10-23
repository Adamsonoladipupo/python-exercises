numbers = [1,2,3,4,5]

def is_square(numbers):
	return numbers **2

square = list(map(is_square, numbers))
print(square)