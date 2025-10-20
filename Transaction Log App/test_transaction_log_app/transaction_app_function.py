def deposit(amount, account_balance):
	account_balance += amount
	return account_balance

def withdraw(amount, account_balance):
	if amount < account_balance:
		account_balance -= amount
	else:
		return account_balance
	return account_balance

def show_transactions(transactions = []):
	for transaction in transactions:
		return transaction

