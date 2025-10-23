words = ["apple", "banana", "kiwi", "grapes", "cherry", ]

def more_than_five(words):
	return len(words) <= 5

new_words = list(filter(more_than_five, words))
print(new_words)
