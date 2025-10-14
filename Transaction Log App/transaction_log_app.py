account_balance = 0
number_of_transactions = 0
deposite_amount = 0
withdraw_amount = 0


def main_menu():
	doc_main_menu = """

	Welcome to Transaction Log App

	1. Deposit
	2. Withdraw
	3. Show Transactions
	4. Exit (-4 to exit)
	"""
	print(doc_main_menu)

	main_menu_options = int(input("Make a selcetion: "))
	match main_menu_options:
		case 1: deposite_menu()
		case 2: withdraw_menu()
		case 3: transaction_history()
		case 4: exitint_app()
	
	
def transaction_history():
	doc_transaction = """
	Transaction History selected ...
	Transactions so far:
	"""
	print(doc_transaction)

def deposite_menu():
	doc_deposite = """

	Deposite selected ...
	How much are you depositing?

	"""
	print(doc_deposite)
	deposite_amount = int(input("Enter amount: "))
	global account_balance
	account_balance = account_balance + deposite_amount
	print(f"You just deposited: {deposite_amount} | New balance: {account_balance}") 

def withdraw_menu():
	doc_withdraw = """

	Withdraw selected ...
	How much are you withdrawing?

	"""
	print(doc_withdraw)
	withdraw_amount = int(input("Enter amount: "))
	global account_balance
	if account_balance < withdraw_amount:
		print("Withdrawal failed: insufficient funds")
	if account_balance > withdraw_amount:
		account_balance = account_balance - withdraw_amount
		print(f"You just withdrew: {withdraw_amount} | New balance: {account_balance}") 

def exitint_app():
	print("")
	global account_balance
	print(f"Final balance: {account_balance}")
	print("Thank you for using Our Transaction Log App")
	main_menu_options = -4



main_menu_options = 1
while main_menu_options != 0 :
	main_menu()