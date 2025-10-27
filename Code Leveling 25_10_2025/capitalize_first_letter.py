names = ['john', 'mary', 'steve']
def capitalize_first_letter(input):
	input = input[0].upper() + input[1:]
	return input

new_list = list(map(capitalize_first_letter, names))
print(new_list)