import random
from book_functions import *

books = ["Atomic Habit", "Magic Fingers", "Clean Coder","a"  ]

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
			print(add_book(user_input, books))
		
		case "3":
			user_input = input("Enter the book title to remove: ")
			removal = remove_book(user_input, books)
			print(removal)

		case "4":
			user_input = input("Enter the old book title: ")
			user_input_new = input("Enter thr new book title: ")
			print(update_book(user_input, user_input_new, books))


		case "5": 
			print("Available Books: ")
			count = 0
			for book in books:
				count +=1
				print(f"{count}. {book}")
		case "6": print(books)

		case _: print("Invalid input, select from the options displayed")