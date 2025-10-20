import MFDS_functions
choice = ""
transactions = []

while True:
	docMain = """

	Welcome to  GBeda Station !

	Available petroleum
	1. Buy Petroleum
	2. Show Transaction History
	3. Exit

	"""
	print(docMain)
	mainMenu = int(input("Enter operation: "))
	match mainMenu:
		case 1:
			docPetroleum = """

	Available petroleum

	1. Petrol  ⇒  ₦650 / Liter
	2. Diesel  ⇒  ₦720 /Liter
	3. Kerosene ⇒  ₦550 /Liter
	4. Gas  ⇒   ₦480 /Liter

			"""
			print(docPetroleum)
			Petroleum = int(input("Enter operation: "))
			match Petroleum:
				case 1: 
					choice = MFDS_functions.buy_petrol(choice, transactions =[])
					transaction = choice
					transactions.append(transaction)
					print(choice)

				case 2: 
					choice = MFDS_functions.buy_diesel(choice)
					print(choice)
				case 3: 
					choice = MFDS_functions.buy_kerosene(choice)
					print(choice)
				case 4: 
					transactions = MFDS_functions.buy_gas(transactions)
					if transactions == []:
						print ("Sorry, you have not made any transactions today")

				case _: print("Invalid input, choose from the options in the list")

		case 2: 
			transactions_history = MFDS_functions.get_transaction_history(transactions = [])
			if transactions == 0:
				print("No transactions yet.")
			else:
				print(transactions)
		case 3: 
			print("Thank you for visiting GBeda Station")
			break
		case _:	
			print("Invalid input, choose from the options in the list")
