def deposit(amount, account_balance, transactions = []):
	account_balance += amount
	transaction = (f"Deposited: ₦{amount} | New Balance: ₦{account_balance}")
	transactions += transaction
	return account_balance

def withdraw(amount, account_balance, transactions = []):
	if amount < account_balance:
		account_balance -= amount
		transaction = (f"Withdrew: ₦{amount} | New Balance: ₦{account_balance}")
	else:
		transaction = ("Withdrawal failed: insufficient funds")
	transactions += transaction
	return account_balance
def show_transactions(transactions = []):
	for transaction in transactions:
		return transaction

