import random

def print_plate_number(list_one, list_two, list_three):
    for item in range(length_of_user_input[0]):
        print(upperCase[item], end="")
    print("-", end="")
    for item in range(length_of_user_input[1]):
        print(numbers[item], end="")
    print("-", end="")
    for item in range(length_of_user_input[2]):
        print((lowerCase[item]).lower(), end="")

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
length_of_user_input = []

user_input = input("Enter a pattern(AAA-###-@@): ")

split_input = user_input.split("-")

for word in split_input:
    length_of_user_input.append(len(word))

upperCase = random.choices(alphabet, k=length_of_user_input[0])
numbers = random.sample(range(1,9),length_of_user_input[1])
lowerCase = random.choices(alphabet, k=length_of_user_input[2])

print_plate_number(upperCase, numbers, lowerCase)




