def return_only_even_numbers(values):
	new_list = []
	for count in range (len(values)):
		if values[count] % 2 == 0:
			new_list += [(values[count])]
	return new_list

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
print(return_only_even_numbers(numbers))