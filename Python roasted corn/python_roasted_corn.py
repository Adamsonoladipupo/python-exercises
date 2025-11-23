numbers = [3,5,8,9,12,44,33,26,39,5]

def legth_of_list(list_input):
    count_number = 0
    for number in list_input:
        count_number += 1
    return count_number

def sum_elements_at_even(list_input):
    sum_number = 0
    for number in range (0,len(list_input),2):
        sum_number += list_input[number]
    return sum_number

def sum_elements_at_odd(list_input):
    sum_number = 0
    for number in range (1,len(list_input), 2):
        sum_number += list_input[number]
    return sum_number

def multiply_every_third_position(list_input):
    multiplied_number = 1
    for count in range (0,len(list_input),3):
        multiplied_number *= list_input[count]
    return multiplied_number

def average(list_input):
    sum_number = 0
    count_number = 0
    for number in range (0,len(list_input)):
        sum_number += list_input[number]
        count_number += 1
    average_number = sum_number / count_number
    return average_number

def maximum(list_input):
    max_number = max(list_input)
    return max_number

def minimum(list_input):
    min_number = min(list_input)
    return min_number




print(minimum(numbers))