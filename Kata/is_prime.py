def is_prime(number):
	factors = 0
	for count in range (2, number):
		if number % count == 0:
			factors = factors + 1
	if factors > 0:
		return print("false")
	else:
		return print("true")

user_input = int(input("Enter a prime number: "))
checker = is_prime(user_input)
print(checker)