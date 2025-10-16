def return_list_of_length(values):
	for count in range (0, len(values)):
		values[count] = len(values[count])
	return values



my_list = ['Alive', 'Bob', 'Charlie']
print(return_list_of_length(my_list))