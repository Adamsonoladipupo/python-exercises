letters = ["1", "2", "3", "4", "5"]
def string_to_integer(input):
	return int(input)

to_numbers = list(map(string_to_integer, letters))
print(to_numbers)
