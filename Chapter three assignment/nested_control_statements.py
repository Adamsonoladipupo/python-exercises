largest_1 = 0
largest_2 = 0
for count in range(10):
	number = int(input("Enter a number: "))
	if number > largest_1:
		largest_1 = number
	if number > largest_2:
		largest_2 = number
print("largest number is: ", largest_1)
print("Second largest number is: ", largest_2)
	