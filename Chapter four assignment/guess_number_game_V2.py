import random

def guess_number_game():
	generated_number = random.randrange(1, 1000)
	number_of_guess = 0
	print(generated_number)
	user_inputs = int(input("Guess my number between 1 and 1000 with the fewest guesses:"))

	while (user_inputs != -1):
		if user_inputs == generated_number:
			number_of_guess += 1
			docstring = """

			Congratulations!!!
			You guessed the number!


			Enter:
			-1 --> To exit
			0 --> To play again
			"""
			print("")
			print("")
			print(f"Number of guesses: {number_of_guess}")
			print(docstring)
			user_inputs = int(input())
			match user_inputs:
				case -1: user_inputs == -1
				case 0: guess_number_game()
		elif user_inputs > generated_number:
			number_of_guess += 1
			user_inputs = int(input("Too high. Try again: "))
		elif user_inputs < generated_number:
			number_of_guess += 1
			user_inputs = int(input("Too low. Try again: "))

guess_number_game()
