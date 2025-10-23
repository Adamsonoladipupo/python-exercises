import random
import book_Selection_System_function

books = []
while True:
	docstring = """
	<--- Acora Book Library! --->
	Welcome to the Book Suggestion System!

 	1. Get Suggestions
 	2. Add Book
 	3. Remove Book
 	4. Update book 
	5. Show all books
	6. Exit

	"""
	print(docstring)
	user_input = int(input("Make a selection: "))
	match user_input:
		case 1: 
			books = book_Selection_System_function.get_books(books)
			print(f"Book title: {random.choice(books)} \nPage: {random.randrange(1, 100)}")
			user_input = input("Would you like to get  another suggestion? (yes/no): ")
			match user_input:
				case "yes":print(f"Book title: {random.choice(books)} \nPage: {random.randrange(1, 100)}")
				case "no": continue
				case _: print("Invalid input, select from the options displayed")
		case 2: book_Selection_System_function.add_book()
		case 3: book_Selection_System_function.remove_book()
		case 4: book_Selection_System_function.update_book()
		case 5: 
			
			book_list = book_Selection_System_function.get_books(books)
			print("All books")
			for count in range (1, len(book_list)):
				print(f"{count} {book_list[count]}")
		case 6: 
			print("Thank you!")
			break