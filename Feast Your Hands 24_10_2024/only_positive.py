numbers = [-2,-1,0,1,2]

def only_positive(input):
	return input >= 0

positive_numbers = list(filter(only_positive, numbers))
print(positive_numbers)