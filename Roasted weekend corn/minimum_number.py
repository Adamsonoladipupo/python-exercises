def minimum_number(values):
	smallest_number = values[0]
	for count in range (len(values)):
		if values[count] < values[0]:
			smallest_number = values[count]
	return smallest_number

numbers = [-20, 200, -382, 1, 212, 98]
smallest_figure = minimum_number(numbers)
print(smallest_figure)