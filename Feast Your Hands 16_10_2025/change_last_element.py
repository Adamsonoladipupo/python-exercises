def change_last_element(value):
	value[-1] = 'yellow'
	return value

colors = ['red', 'green', 'blue']
print(change_last_element(colors))