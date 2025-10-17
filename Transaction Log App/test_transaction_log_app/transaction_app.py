import transaction_app_function

account_balance = 0

while True:
	doc_main_menu = """

	Welcome to Transaction Log App
 	1. Deposit
 	2. Withdraw
 	3. Show Transactions
 	4. Exit

	"""
	print (doc_main_menu)
	user_input = int(input("Enter your choice: "))
	match user_input:
		case 1: 
			amount = int(input("Enter deposit amount: "))
			account_balance = transaction_app_function.deposit(amount, account_balance, transactions = [])
			transactions = transactions[]
			print(transactions)
		case 2: 
			amount = int(input("Enter withdrawal amount: "))
			account_balance = transaction_app_function.withdraw(amount, account_balance, transactions = [])
			transactions = (f"Withdrew: ₦{amount} | New Balance: ₦{account_balance}")
			print(transactions)
			