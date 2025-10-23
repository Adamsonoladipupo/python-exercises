from functools import reduce

words = ["I", "Love", "Python", "Snacks"]

def add_hyphen(word1, word2):
	return word1 + "-" + word2

result = reduce(add_hyphen, words)
print(result)