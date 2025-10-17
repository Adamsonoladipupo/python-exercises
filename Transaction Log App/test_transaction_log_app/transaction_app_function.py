account_balance = 0
def deposit(amount, account_balance, transactions = [] ):
	account_balance += amount
	transactions += (f"Deposited: ₦{amount} | New Balance: ₦{account_balance}")
	return account_balance

def withdraw(amount, account_balance, transactions = []):
	if amount < account_balance:
		account_balance -= amount
		transactions += (f"Withdrew: ₦{amount} | New Balance: ₦{account_balance}")
	else:
		transactions += ("Withdrawal failed: insufficient funds")
	#transactions += transaction
	return account_balance