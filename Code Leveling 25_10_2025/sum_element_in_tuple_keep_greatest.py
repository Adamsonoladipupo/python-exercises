numbers = [(1, 2), (3, 4), (5, 6)]

def sum_tuple_element(inputs):
	tempVar = 0
	count = 0
	for input in inputs:
		for each in input:
			tempVar +=each
		inputs[count] = tempVar
		count+=1
		tempVar = 0
	return inputs

def number_greater_than_five(values):
	#values = sum_tuple_element(values)
	return values > 5

new_list = sum_tuple_element(numbers)

new_list_greaterthan_five = list(filter(number_greater_than_five,numbers))

print(new_list)
print(new_list_greaterthan_five)