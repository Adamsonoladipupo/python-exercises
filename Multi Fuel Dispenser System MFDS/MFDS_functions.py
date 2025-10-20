def buy_petrol(choice):
	choice = input("choose input type: liter or amount: ")
	receipt = ""
	if choice == "liter":
		input_liter = int(input("How Many Liters of petrol are you buying (₦650/L): "))
		cost_of_petrol = input_liter * 650

		receipt = f"""

		Customers Transaction Receipt
		=========================================
		= Product : Petrol        		=
		= Amount : ₦{cost_of_petrol: .2f}        	=
		= Liters : {input_liter: .2f}L        	=
		= Thank you For your Petronage 		=
		=========================================

		Saving Transaction History. . . ...

		"""
		return receipt

	if choice == "amount":
		input_amount = int(input("How much petrol are you buying (₦650/L): "))
		amount_of_petrol = input_amount / 650

		receipt = f"""

		Customers Transaction Receipt
		=========================================
		= Product : Petrol        		=
		= Amount : ₦{input_amount: .2f}        	=
		= Liters : {amount_of_petrol: .2f}L        	=
		= Thank you For your Petronage 		=
		=========================================

		Saving Transaction History. . . ...

		"""
		return receipt

	return choice
	

def buy_diesel(choice):
	choice = input("choose input type: liter or amount: ")
	receipt = ""
	if choice == "liter":
		input_liter = int(input("How Many Liters of petrol are you buying (₦720/L): "))
		cost_of_petrol = input_liter * 720

		receipt = f"""

		Customers Transaction Receipt
		=========================================
		= Product : Diesel        		=
		= Amount : ₦{cost_of_petrol: .2f}        	=
		= Liters : {input_liter: .2f}L        	=
		= Thank you For your Petronage 		=
		=========================================

		Saving Transaction History. . . ...

		"""
		return receipt

	if choice == "amount":
		input_amount = int(input("How much petrol are you buying (₦720/L): "))
		amount_of_petrol = input_amount / 720

		receipt = f"""

		Customers Transaction Receipt
		=========================================
		= Product : Diesel        		=
		= Amount : ₦{input_amount: .2f}        	=
		= Liters : {amount_of_petrol: .2f}L        	=
		= Thank you For your Petronage 		=
		=========================================

		Saving Transaction History. . . ...

		"""
		return receipt

	return choice


def buy_kerosene(choice):
	choice = input("choose input type: liter or amount: ")
	receipt = ""
	if choice == "liter":
		input_liter = int(input("How Many Liters of petrol are you buying (₦550/L): "))
		cost_of_petrol = input_liter * 550

		receipt = f"""

		Customers Transaction Receipt
		=========================================
		= Product : Kerosene        		=
		= Amount : ₦{cost_of_petrol: .2f}        	=
		= Liters : {input_liter: .2f}L        	=
		= Thank you For your Petronage 		=
		=========================================

		Saving Transaction History. . . ...

		"""
		return receipt

	if choice == "amount":
		input_amount = int(input("How much petrol are you buying (₦550/L): "))
		amount_of_petrol = input_amount / 550

		receipt = f"""

		Customers Transaction Receipt
		=========================================
		= Product : kerosene        		=
		= Amount : ₦{input_amount: .2f}        	=
		= Liters : {amount_of_petrol: .2f}L        	=
		= Thank you For your Petronage 		=
		=========================================

		Saving Transaction History. . . ...

		"""
		return receipt

	return choice
	

def buy_gas(choice):
	choice = input("choose input type: liter or amount: ")
	receipt = ""
	if choice == "liter":
		input_liter = int(input("How Many Liters of petrol are you buying (₦480/L): "))
		cost_of_petrol = input_liter * 480

		receipt = f"""

		Customers Transaction Receipt
		=========================================
		= Product : Gas        		=
		= Amount : ₦{cost_of_petrol: .2f}        	=
		= Liters : {input_liter: .2f}L        	=
		= Thank you For your Petronage 		=
		=========================================

		Saving Transaction History. . . ...

		"""
		return receipt

	if choice == "amount":
		input_amount = int(input("How much petrol are you buying (₦480/L): "))
		amount_of_petrol = input_amount / 480

		receipt = f"""

		Customers Transaction Receipt
		=========================================
		= Product : Gas       		=
		= Amount : ₦{input_amount: .2f}        	=
		= Liters : {amount_of_petrol: .2f}L        	=
		= Thank you For your Petronage 		=
		=========================================

		Saving Transaction History. . . ...

		"""
		return receipt

	return choice


def get_transaction_history(transactions = []):
	return transactions
