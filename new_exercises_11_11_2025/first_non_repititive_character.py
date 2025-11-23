def get_non_repitition(input):
	unique_letter = ""
	checker = ""
	count = 0
	for char in input:
		checker = char
		for letter in input:
			unique_letter = letter
			if char == unique_letter:
				count+=1
		if count == 1:
			return char
			break
		count = 0

word = "dmadam"
print(get_non_repitition(word))