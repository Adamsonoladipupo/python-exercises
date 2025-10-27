words =  ['cat', 'elephant', 'tiger', 'lion']

def get_words_longerthan_five(inputs):
	return words > 5

new_words = list(filter(get_words_longerthan_five, words))
print(new_words)