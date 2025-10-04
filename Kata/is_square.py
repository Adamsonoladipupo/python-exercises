def is_square(number):
	if (number ** 0.5) % 1 == 0:
		print ("true")
	else:
		print("false")
	return 0

user_input = int(input("Check for perfect square: "))
result = is_square(user_input)
print(result)
	