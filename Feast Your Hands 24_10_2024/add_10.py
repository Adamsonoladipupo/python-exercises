numbers = [0, 5, 10, 15]
def add_10(input):
	return input + 10
added = list(map(add_10, numbers))
print(added)