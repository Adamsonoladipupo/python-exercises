def return_three_characters(values):
	new_list = []
	for count in range (len(words)):
		if len(words[count]) > 3:
			new_list += [(words[count])]
	return new_list


words = ["lamb", "kit", "yam", "kings", "dogs", "man"]
print(return_three_characters(words))
