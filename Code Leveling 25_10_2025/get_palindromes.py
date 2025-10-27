words = ['level', 'world', 'madam', 'python']
def get_palindrome(inputs):
	return inputs == input[::-1]
new_list = list(filter(get_palindrome,words))
print(new_list)