tuple = ('apple', 'banana', 'cherry')

def tuple_to_list(inputs):
	new_list = []
	new_tuple = ()
	for input in inputs:
		new_list.append(input)
	new_list.append("mango")
	for count in range (0, len(new_list)):
		for item in new_list:
			new_tuple = (new_list[count])
	return new_list, new_tuple
	

print(tuple_to_list(tuple))
	