import transaction_app_function

account_balance = 0
transactions = []

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
			account_balance = transaction_app_function.deposit(amount, account_balance)
			transaction = f"Deposited: ₦{amount} | New Balance: ₦{account_balance}"
			print(transaction)
			transactions.append(transaction)
		case 2: 
			amount = int(input("Enter withdrawal amount: "))
			account_balance = transaction_app_function.withdraw(amount, account_balance)
			if amount < account_balance:
				transaction = (f"Withdrew: ₦{amount} | New Balance: ₦{account_balance}")
				print(transaction)
				transactions.append(transaction)
			else: 
				transaction = ("Withdrawal failed: insufficient funds")
				print(transaction)
				transactions.append(transaction)

		case 3: 
			if transactions == 0:
				print("No transactions yet.")
			else:
				print("Transactions so far")
				for count in range (len(transactions)):
					print(f" {count +1} {transactions[count]}")
		case 4: 
			print(f"Final Balance ₦{account_balance} \nThank you for using Transaction Log App!")
			break
				
			