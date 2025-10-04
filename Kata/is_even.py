def is_even(number):
	return number % 2 == 0

user_input = int(input("Enter number: "))
checker = is_even(user_input)
print(checker)
			