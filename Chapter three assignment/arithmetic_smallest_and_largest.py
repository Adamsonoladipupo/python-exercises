sum = 0
product = 1
minimum = 0
maximum = 0
average = 0
for count in range (4):
	user_input = int(input("Enter a number: "));
	sum += user_input
	product *= user_input
	if user_input >= minimum:
		minimum = user_input
		if user_input <= minimum:
			 minimum = user_input
	if user_input>maximum:
		maximum = user_input
average = sum/4
	
print(f"Sum of numbers is: {sum}")
print(f"product of numbers is: {product}")
print(f"Maximum number is: {maximum}")
print(f"Minimu number is: {minimum}")
print(f"Average of the numbers is: {average}")