print("Welcome! This number helps you sort numbers in ascending order")
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
number_3 = float(input("Enter third number: "))

acsending_1 = 0
acsending_2 = 0
acsending_3 = 0

if number_2 < number_1 > number_3 or number_1 < number_1 > number_2:
	acsending_3 = number_1
elif number_1 < number_2 > number_3 or number_3 < number_2 > number_2:
	acsending_3 = number_2
else : 
	acsending_3 = number_3

if number_2 > number_1 < number_3 or number_3 > number_1 < number_2:
	acsending_1 = number_1
elif number_1 > number_2 > number_3 or number_3 > number_2 > number_1:
	acsending_1 = number_2
else:
	acsending_1 = number_3

if number_2 > number_1 > number_3 or number_3 > number_1 > number_2 :
	acsending_2 = number_1
elif number_1 > number_2 > number_3 or number_3 > number_2 > number_1:
	acsending_2 = number_2
else:
	acsending_2 = number_3

print(acsending_1)
print(acsending_2)
print(acsending_3)
