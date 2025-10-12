 
def sum_square_all_element(values):
	summation = 0
	for count in range(len(values)):
		values[count] = values[count]**2
		summation += values[count]
	return summation
		

sample_data = [2, 3, 4, 5, 7]
result = sum_square_all_element(sample_data)
print(result)