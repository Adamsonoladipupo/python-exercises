def factors_of(number):
	factors = 0
	for count in range (1, number+1):
		if number % count == 0:
			factors = factors + 1
	return factors

user_input = int(input("Enter a number: "))
check = factors_of(user_input)
print("There are", check ,"factors")