import random

#def computer_assisted_instruction(numbers)

for count in range(2):
	first_number = random.randrange(1, 9)
	second_number = random.randrange(1, 9)
answer = first_number * second_number
user_answer = 0
print(f"How much is {first_number} times {second_number}?")
while(answer != user_answer):
	user_answer = int(input("Enter your answer: "))
	if answer == user_answer:
		print("Correct!!! Very good!")
	else:
		print("No. Please try again.")
