from functools import reduce

dictionaries = [{'a': 1}, {'b': 2}, {'c': 3}]

def add_dictionaries(input, inputs):
	return input + inputs
dictionary = reduce(add_dictionaries, dictionaries)
print(dictionary)