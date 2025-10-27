prices = [100, 200, 300]
def add_10_percent(input):
	input = input + (input*(10/100))
	return input

new_prices = list(map(add_10_percent, prices))
print(new_prices)