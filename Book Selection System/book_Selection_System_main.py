import random

def main_menu():
	display_menu = """
	
	Welcome to ACORA Books
	1. Get book suggesttions
	2. Add books
	3. Remove books
	4. Update books
	5. Show all books
	
	"""
	return display_menu

def suggest_books(inputs):
	suggestion_display =f"""

	Book title: {random.choice(inputs)}
	Book page: {random.randrange(1, 100)}

	""" 
	return suggestion_display


books = ["Atomic Habit", "Magic Finger" ]

#def add_books():

while True:
	print(main_menu())

	user_input = input("Make a selection: ")
	match user_input:
		case "1": 
			print(suggest_books(books))
			while True:
				user_input = input("Get more selections(yes/no): ")
				match user_input:
					case "yes": print(suggest_books(books))
					case "no": break
					case _: print("Invalid input, select from the options displayed")
					
		case "2": 
			user_input = input("Enter the book title: ")
			books.append(user_input)
			print(f"{user_input} added successfully!")
		
		case "3": print("3")
		case "4": print("4")
		case "5": 
			print("Available Books: ")
			count = 0
			for book in books:
				count +=1
				print(f"{count}. {book}")

		case _: print("Invalid input, select from the options displayed")

print("End not in the main loop")


