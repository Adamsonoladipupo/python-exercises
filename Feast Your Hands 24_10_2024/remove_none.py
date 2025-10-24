lists =  [1, None, 3, None, 5]

def remove_none(input):
	return input

new_lists = (list(filter(remove_none, lists)))
print(new_lists)