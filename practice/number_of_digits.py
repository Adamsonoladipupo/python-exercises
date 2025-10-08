user_input = int(input("Enter a number: "))
digit_count = 1
while user_input > 9:
	single_number = user_input % 10
	user_input = user_input // 10
	digit_count = digit_count + 1
print (digit_count, "digit(s)")
	