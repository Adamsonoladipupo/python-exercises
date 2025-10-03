def divide_or_square_root(a):
	if a <= 0:
		return print("Invalid input")
	else:
		if a % 5 == 0:
			a = a ** 0.5
		else:
			a = a % 5
	return a


number = int(input("Enter number 1: "))
result = divide_or_square_root(number)
print(result)
