list =  [ [2, 3, 4],  [1, 5, 7],  [4, 6, 8], [5,5,5]]

def sum_2D_list_element(input):
	count = 0
	temVar = 0
	for item2 in input:
		for item in item2:
			temVar +=item
		input[count] = temVar
		count +=1
		temVar = 0
	return input

print(sum_2D_list_element(list))	
