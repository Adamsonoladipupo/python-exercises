tuple = (10, 20, 30, 40)
def unpack(input):
	first_varaible, second_varaible, *others = tuple
	return first_varaible, second_varaible, others

print(unpack(tuple))