def is_odd(number):
	return number % 2 != 0

user_input = int(input("Enter a number: "))
check = is_odd(user_input)
print(check)