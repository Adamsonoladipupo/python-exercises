factorial = 1
user_input = int(input("Enter a number: "))
for count in range (1, user_input):
	count+=1
	factorial = factorial * count
print(f"The factorial of {user_input} is: {factorial}")