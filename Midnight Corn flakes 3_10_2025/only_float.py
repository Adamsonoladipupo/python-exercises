def only_float(a, b):
	if a % 1 != 0 and b % 1 != 0:
		return print("2: Both are float") 
	elif a % 1 != 0 or b % 1 != 0:
		return print("1: One float")
	else:
		return print("0: no float")
	

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

only_float(num1, num2)
	
