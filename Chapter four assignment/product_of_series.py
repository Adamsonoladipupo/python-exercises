def product_of_series(*numbers):
	product_of_numbers = 1
	for count in numbers:
		product_of_numbers *= count
	return product_of_numbers


print(product_of_series(2,4,6,7))