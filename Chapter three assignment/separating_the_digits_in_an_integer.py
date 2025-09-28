user_input = int(input("Enter a 5digits number: "))
divider = 10000
digits_number= 0

for count in range(5):
	digits_number = user_input % 10
	user_input //= 10
	print (digits_number, end=" ")