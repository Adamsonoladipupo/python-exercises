def buy_petrol_with_price(price):
	liter = price / 650
	return liter

def buy_petrol_with_liter(liter):
	price = liter * 650
	return price

def buy_diesel_with_price(price):
	liter = price / 720
	return liter

def buy_diesel_with_liter(liter):
	price = liter * 720
	return price

def buy_kerosene_with_price(price):
	liter = price / 550
	return liter

def buy_kerosene_with_liter(liter):
	price = liter * 550
	return price

def buy_gas_with_price(price):
	liter = price / 480
	return liter

def buy_gas_with_liter(liter):
	price = liter * 480
	return price

def get_transaction_history(transactions = []):
	return transactions