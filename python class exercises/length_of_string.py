def is_length(value):
	count = 0;
	for length in value:
		count = count + 1
	return count

user_input = str(input("Enter a string: "))
length = is_length(user_input)
print(length)