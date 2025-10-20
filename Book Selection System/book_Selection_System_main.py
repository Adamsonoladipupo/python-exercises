import book_Selection_System_function

while True:
	docstring = """
	Welcome to the Book Suggestion System!
 	1. Get Suggestions
 	2. Add Book
 	3. Remove Book
 	4. Update book 
	5. Show all books
	6. Exit
	"""
	print(docstring)
	user_input = int(input("Make a selection"))
	match user_input:
		case 1: book_Selection_System_function.get_suggestion()
		case 2: book_Selection_System_function.add_book()
		case 3: book_Selection_System_function.remove_book()
		case 4: book_Selection_System_function.update_book()
		case 5: book_Selection_System_function.get_books()
		case 6: 
			print("Thank you!")
			break
	