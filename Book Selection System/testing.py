import random
books = ["The Hobbit", "The Mystery", "Atomic Habit", "Things Fall Apart" ]

while True:
	select = input("Get a suggestion: ")
	match select:
		case "YES": print(f"book title: {random.choice(books)} \nPage: {random.randrange(1, 100)}")
		case "no": print("Alrigth then")
		case _: print("invalid selection")
