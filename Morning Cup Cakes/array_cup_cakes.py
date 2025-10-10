import random

def is_smallest(numbers):
	numbers[0] = smallest = numbers[0]
	for count in range (len(numbers)):
		if numbers[count] < smallest:
			smallest = numbers[count]
	return smallest


def is_average(numbers):
	average = 0
	for count in range (len(numbers)):
		average += numbers[count]
	count+=1
	average = average / count
	return average

def count_occurence(numbers):
	occurence = 0
	focus_number = numbers[6]
	for count in range (len(numbers)):
		if focus_number == numbers[count]:
			occurence += 1
	return occurence

def contains_element(numbers):
	target_number = 9
	check = False
	for count in range (len(numbers)):
		if target_number == numbers[count]:
			check = True
	return check

def get_first_element(numbers):
	if numbers == 0:
		return numbers
	if numbers != 0:
		return numbers[0]
	return numbers

def get_last_element(numbers):
	if numbers == 0:
		return numbers
	if numbers != 0:
		return numbers[len(numbers) - 1]
	return numbers

def array_length(numbers):
	length = 0
	while numbers != 0:
		numbers.pop
		length += 1
	return length
		

def get_middle_element(numbers):
	if len(numbers) % 2 != 0:
		return numbers[len(numbers) //2]
	else:
		return numbers[len(numbers) //2-1]
	return numbers

def swap_first_and_last(number):
	temporary_variable = numbers[0]
	numbers[0] = numbers[len(numbers) - 1]
	numbers[len(numbers) - 1] = temporary_variable	
	return numbers

# Home Snacks Assignment 

def random_list(numbers):
	for count in range (10):
		numbers += random.randrange(1, 50)
	return numbers

#def get_length(numbers):
	
def sum_even(numbers):
	sum_of_even = 0
	for count in range(1, len(numbers), 2):
		sum_of_even += numbers[count]
		
	return sum_of_even

def sum_odd(numbers):
	sum_of_odd = 0
	for count in range(0, len(numbers), 2):
		sum_of_odd += numbers[count]
		
	return sum_of_odd

def multiply_third_position(numbers):
	multiply_third = 1
	for count in range(0, len(numbers), 3):
		multiply_third *= numbers[count]
		
	return multiply_third

def all_average(numbers):
	average = 0
	for count in range (len(numbers)):
		average += numbers[count]
	count+=1
	average = average / count
	return average

def is_smallest(numbers):
	numbers[0] = smallest = numbers[0]
	for count in range (len(numbers)):
		if numbers[count] < smallest:
			smallest = numbers[count]
	return smallest

def is_largest(numbers):
	numbers[0] = largest = numbers[0]
	for count in range (len(numbers)):
		if numbers[count] > largest:
			largest = numbers[count]
	return largest

def strings_length(strings):
	if len(strings) >= 2 and strings[0] == strings[len(strings)-1]:
		return strings
	
"""
sequenctial_integers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(sequenctial_integers)
"""

def add_third_position(numbers):
	add_third = 1
	for count in range(0, len(numbers), 3):
		add_third += numbers[count]
		
	return add_third

def sum_of_first_middle_last(numbers):
	summation = 0
	middle_number = 0
	if (len(numbers) % 2 != 0):
		middle_number = numbers[int(len(numbers) / 2)]
	if (len(numbers) % 2 == 0):
		middle_number = (numbers[int(len(numbers) / 2)-1] + numbers[int(len(numbers) / 2)]) / 2
	summation = numbers[0] + middle_number + numbers[len(numbers)-1]
	return summation


numbers = [10,9,11,8,  4,  3,2,12,4]
#strings = ['she', 'good', 'book', 'she']
result = sum_of_first_middle_last(numbers)
print(result)


