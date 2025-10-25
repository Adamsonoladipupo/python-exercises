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

def add_book(input, books):
	message = ""
	if input.lower() in books:
		message = f"'{input}' already exit"
	if input.lower() not in books:
		books.append(input)
		message = f"'{input}' added successfully"
	return message


def remove_book(input, books):
	message = ""
	if input in books:
		books.remove(input)
		message = f"'{input}' removed successfully"
	else:
		message = f"'{input}' does not exit"
	return message

def update_book(input, new_input, books):
	index_of_book = books.index(input)
	books[index_of_book] = new_input
	return "Book updated successfully"
