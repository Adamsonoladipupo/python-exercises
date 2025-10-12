def longest_word(words):
	longest_word = words[0]
	for count in range (len(words)):
		if len(words[count]) > len(words[0]):
			longest_word = len(words[count])
	return longest_word

inputs =  ['welcome', 'out',  'breakfast', 'weather', 'mobile', 'trypanosomiasis', 'journey']
result = longest_word(inputs)
print(result)