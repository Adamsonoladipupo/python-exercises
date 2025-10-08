def sapa_size():
	doc_sapa = """

	Sapa size selected ...
	Cost: $2,500 per pizza box (4 slices)

	How many guest are you inviting
	
	"""
	print(doc_sapa)
	guest = int(input())
	box = guest/4
	if box % 1 != 0:
		box = box + 1	
		box = int(box)
	cost = box * 2500
	left_over = (box * 4) - guest
	print(f"You will be buying {box} box(s) of pizza")
	print(f"it cost: ${cost}")
	print(f"Leftover slice(s): {left_over}")

def small_money():
	doc_sapa = """

	Small Money selected ...
	Cost: $2,900 per pizza box (6 slices)

	How many guest are you inviting
	
	"""
	print(doc_sapa)
	guest = int(input())
	box = guest/6
	if box % 1 != 0:
		box = box + 1	
		box = int(box)
	cost = box * 2900
	left_over = (box * 6) - guest
	print(f"You will be buying {box} box(s) of pizza")
	print(f"it cost: ${cost}")
	print(f"Leftover slice(s): {left_over}")

def big_boys():
	doc_sapa = """

	Big boys size selected ...
	Cost: $4,000 per pizza box (8 slices)

	How many guest are you inviting
	
	"""
	print(doc_sapa)
	guest = int(input())
	box = guest/8
	if box % 1 != 0:
		box = box + 1	
		box = int(box)
	cost = box * 4000
	left_over = (box * 8) - guest
	print(f"You will be buying {box} box(s) of pizza")
	print(f"it cost: ${cost}")
	print(f"Leftover slice(s): {left_over}")

def odogwu():
	doc_sapa = """

	Odogwu size selected ...
	Cost: $5,200 per pizza box (12 slices)

	How many guest are you inviting
	
	"""
	print(doc_sapa)
	guest = int(input())
	box = guest/12
	if box % 1 != 0:
		box = box + 1	
		box = int(box)
	cost = box * 5200
	left_over = (box * 12) - guest
	print(f"You will be buying {box} box(s) of pizza")
	print(f"it cost: ${cost}")
	print(f"Leftover slice(s): {left_over}")

def main_menu():
	pizza_wahala = """

		Welcome to Pizza Wahala Joint!
	
		 ________________________________________________  
		| Pizza Type  | Number of slices | price per box |
		 ------------------------------------------------
		| Sapa size   | 4		 | 2,500	 |
		 ------------------------------------------------
		| Small Money | 6		 | 2,900	 |
		 ------------------------------------------------
		| Big boys    | 8		 | 4,000	 |
		 ------------------------------------------------
		| Odogwu      | 12		 | 5,200	 |
		 ------------------------------------------------

		Select a pizza type.
		1-> Sapa size
		2-> Small money
		3-> Big boys
		4-> Odogwu

	"""

	print (pizza_wahala)
	pizza_main_menu = input()
	match pizza_main_menu:
		case "1": sapa_size()
		case "2": small_money()
		case "3": big_boys()
		case "4": odogwu()
		case _:	
			print("Invalid input, select from the menu options") 
			main_menu()
				

main_menu()
