numbers = list(range(1,16))
new_list = numbers.copy()
print(numbers)


def sum_of_first_middle_third_element(number_list):
    total = 0
    middle_number = 0
    if len(numbers) % 2 != 0:
        middle_number = number_list[len(number_list) // 2]
    else:
        middle_number = number_list[len(number_list) // 2] + number_list[len(number_list) // 2 - 1] / 2
    total = number_list[0] + number_list[len(number_list)-1] + middle_number
    return total

def add_every_third_element(numbers):
    sum_of_numbers = 0
    for element in range(0,len(numbers),3):
        sum_of_numbers += numbers[element]
    return sum_of_numbers

print(sum_of_first_middle_third_element(numbers))