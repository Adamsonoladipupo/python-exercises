def remove_odd_index(values):
	new_set = ''
	for count in range(1, len(values), 2):
		new_set += (values[count])
	return new_set

letters = "semicolon"
result = remove_odd_index(letters)
print(result)