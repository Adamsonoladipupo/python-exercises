list_tuple =  [(1, 'A'), (4, 'B'), (2, 'C')]
def get_value_greater_than_two(inputs):
	return input in inputs > 0

new_collection = list(filter(get_value_greater_than_two, list_tuple))
print(new_collection)