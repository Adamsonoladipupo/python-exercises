 
def square_all_element(values):
	for count in range(len(values)):
		values[count] = values[count]**2
	return values
		

sample_data = [2, 3, 4, 5, 7]
result = square_all_element(sample_data)
print(result)