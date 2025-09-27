number_of_failure = 0
number = 0
while number !=1 and number !=2 :
	number = int(input("Enter a number: "))
	if number != 1 and number != 2:
		number_of_failure += 1

print("number of failures", number_of_failure)
