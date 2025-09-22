first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

second_highest_number = 0

if third_number > second_number > first_number or first_number > second_number > first_number :
	second_highest_number = second_number
if second_number > third_number > first_number or first_number > third_number > second_number:
	second_highest_number = third_number
if third_number > first_number > second_number or second_number > first_number > third_number:
	second_highest_number = first_number

print("The second highest number is: ", second_highest_number)