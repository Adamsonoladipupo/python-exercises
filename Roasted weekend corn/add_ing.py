def add_ing(letters):
	if len(letters) < 3:
		letters = letters
	elif len(letters) >= 3:
		if letters[-1] == 'g' and letters[-2] == 'n' and letters[-3] == 'i' :
			letters = letters + 'ly'
		else: 
			letters = letters + 'ing'
	return letters

letters = 'willng'
result = add_ing(letters)
print(result)