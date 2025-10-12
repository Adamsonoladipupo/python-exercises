def repeat_strings(values):
	new_set = ''
	if values[1] % 1 == 0:
		new_set =  values[0] * values[i]
		return new_set
	else:
		return values

values = []
values[0] = input("Enter a string: ")
values[1] = int(input("enter a number: "))

result = repeat_strings(values)
print(result)