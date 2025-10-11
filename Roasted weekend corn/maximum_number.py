def maximum_number(values):
	maximum_number = values[0]
	for count in range (len(values)):
		if values[count] > values[0]:
			maximum_number = values[count]
	return maximum_number

numbers = [8, 4, 9, 2, 5, 7, 3]
maximum_figure = maximum_number(numbers)
print(maximum_figure)