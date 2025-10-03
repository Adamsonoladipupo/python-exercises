def my_discount(price, discount):
	new_price = price - (price*(discount/100))
	return new_price


commodity_price = int(input("Enter price: "))
seller_discount = int(input("Enter discount: "))

discounted_price = my_discount(commodity_price, seller_discount)
print("You new price is: ", discounted_price)