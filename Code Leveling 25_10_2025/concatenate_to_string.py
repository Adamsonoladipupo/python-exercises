from functools import reduce
word_list = ['I', 'love', 'Python']
def concatenate(input, inputs):
	return input + " " + inputs

sentence = reduce(concatenate, word_list)
print(sentence)