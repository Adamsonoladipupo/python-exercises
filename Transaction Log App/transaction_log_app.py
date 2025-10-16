def main_menu(amount, account_balance, transactions = []):
	doc_main_menu = """

	Welcome to Transaction Log App

	1. Deposit
	2. Withdraw
	3. Show Transactions
	4. Exit
	"""
	print(doc_main_menu)

	main_menu_options = int(input("Make a selcetion: "))
	match main_menu_options:
		case 1: 
			amount = int(input("Enter amount: "))
			deposit(amount, account_balance)
		case 2: 
			amount = int(input("Enter amount: "))
			withdraw(amount, account_balance)
		case 3: transaction_history()
		case 4: a

def deposit(amount, account_balance, transactions = []):
	account_balance += + amount
	transactions = (f"Deposited:₦{amount} | New Balance:₦{account_balance}") 
	print(transactions)
	return account_balance

def withdraw(amount, account_balance, transactions = []):
	if amount > account_balance:
		print("Withdrawal failed: insufficient funds")
	elif amount < account_balance:
		account_balance -= amount
		return New Balance:₦{account_balance}") 
	print(transactions)

def exit_app():
	print("")
	print(f"Final balance: {account_balance}")
	print("Thank you for using Our Transaction Log App")
	more_option = A


account_balance = 100
amount = 0
transactions = []
while amount != -1 :
	main_menu(amount, account_balance)


