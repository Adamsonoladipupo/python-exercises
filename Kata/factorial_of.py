def factorial_of(number):
	factorial = 1
	for count in range(1, number+1):
		factorial = factorial * count
	return factorial

user_input = int(input("Enter a number: "))
result = factorial_of(user_input)
print(result)