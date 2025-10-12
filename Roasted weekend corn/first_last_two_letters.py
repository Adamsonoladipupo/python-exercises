def first_last_two_letters(letters):
	new_set = ""
	if len(letters) < 2:
		return new_set
	first_two_last_two = strings[0] + strings[1] + strings[-2] + strings[-1]
	new_set += first_two_last_two 
	return new_set

strings = 'rpe'
result = first_last_two_letters(strings)
print(result)