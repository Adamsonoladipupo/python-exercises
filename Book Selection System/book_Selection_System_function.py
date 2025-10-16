def get_suggestion():
	print("Book of the day")
	print("Book title: The Habbit")
	print("Page: 34")

	user_input = str(input("Would you like to get  another suggestion? (yes/no): "))
	...

def add_book():
	user_input = str(input(" Enter the book title: "))

def remove_book():
	user_input = str(input(" Enter the book title to remove: "))

def update_book():
	user_input = str(input("Enter the old title: "))
	user_input = str(input("Enter the new title: "))

def get_books():
	books = ["The Hobbit", "The Mystery", "Animal Farm", "Brave kingdom" ]
	docBooks = """
	All Books
 	1. The Hobbit
 	2. The Mystery
 	3. Animal Farm
 	4. Brave kingdom
 	5. . . . . . . . . . . .
	"""
	print(docBooks)
	