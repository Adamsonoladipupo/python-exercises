import MFDS_function
price = 0
liter = 0
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
	mainMenu = input("Enter operation: ")
	match mainMenu:
		case "1":
			docPetroleum = """

	Available petroleum

	1. Petrol  ⇒  ₦650 / Liter
	2. Diesel  ⇒  ₦720 /Liter
	3. Kerosene ⇒  ₦550 /Liter
	4. Gas  ⇒   ₦480 /Liter

			"""
			print(docPetroleum)
			Petroleum = input("Enter operation: ")
			match Petroleum:
				case "1": 
					buy_options = input("choose input type (liter or amount): ")			
					if buy_options == "amount":
						price = int(input("How much petrol are you buying: "))
						liter = MFDS_function.buy_petrol_with_price(price)

					if buy_options == "liter":
						liter = int(input("How many liter(s) of petrol are you buying: "))
						price = MFDS_function.buy_petrol_with_liter(liter)

					receipt = f"""

	Customers Transaction Receipt
	========================================
	= Product : Petrol  				
	= Amount : ₦{price: .2f}        				
	= Liters : {liter: .2f}L        				
	= Thank you For your Petronage 			
	========================================
	Saving Transaction History. . . ...
					"""
					print(receipt)
					transactions.append(receipt)

				case "2": 

					buy_options = input("choose input type (liter or amount): ")			
					if buy_options == "amount":
						price = int(input("How much diesel are you buying: "))
						liter = MFDS_function.buy_diesel_with_price(price)

					if buy_options == "liter":
						liter = int(input("How many liter(s) of diesel are you buying: "))
						price = MFDS_function.buy_diesel_with_liter(liter)

					receipt = f"""

	Customers Transaction Receipt
	========================================
	= Product : Diesel  				
	= Amount : ₦{price: .2f}        				
	= Liters : {liter: .2f}L        				
	= Thank you For your Petronage 			
	========================================
	Saving Transaction History. . . ...
					"""
					print(receipt)
					transactions.append(receipt)


				case "3": 
					buy_options = input("choose input type (liter or amount): ")			
					if buy_options == "amount":
						price = int(input("How much kerosene are you buying: "))
						liter = MFDS_function.buy_kerosene_with_price(price)

					if buy_options == "liter":
						liter = int(input("How many liter(s) of kerosene are you buying: "))
						price = MFDS_function.buy_kerosene_with_liter(liter)

					receipt = f"""

	Customers Transaction Receipt
	========================================
	= Product : kerosene  				
	= Amount : ₦{price: .2f}        				
	= Liters : {liter: .2f}L        				
	= Thank you For your Petronage 			
	========================================
	Saving Transaction History. . . ...
					"""
					print(receipt)
					transactions.append(receipt)

				case "4": 
					buy_options = input("choose input type (liter or amount): ")			
					if buy_options == "amount":
						price = int(input("How much gas are you buying: "))
						liter = MFDS_function.buy_gas_with_price(price)

					if buy_options == "liter":
						liter = int(input("How many liter(s) of gas are you buying: "))
						price = MFDS_function.buy_gas_with_liter(liter)

					receipt = f"""

	Customers Transaction Receipt
	========================================
	= Product : Gas				
	= Amount : ₦{price: .2f}        				
	= Liters : {liter: .2f}L        				
	= Thank you For your Petronage 			
	========================================
	Saving Transaction History. . . ...
					"""
					print(receipt)
					transactions.append(receipt)

				case _: print("Invalid input, choose from the options in the list")

		case "2": 
			transactions_history = MFDS_function.get_transaction_history(transactions = [])
			if len(transactions) > 0:
				for count in transactions:
					print(count)
			if transactions == []:
				print("Sorry, you have not made any transactions today")

		case "3": 
			print("Thank you for visiting GBeda Station")
			break
		case _:	
			print("Invalid input, choose from the options in the list")
