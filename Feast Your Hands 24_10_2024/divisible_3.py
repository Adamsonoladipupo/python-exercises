numbers = [1, 3, 4, 6, 9, 12]
def divisible_3(input):
	return input%3 == 0

new_list = list(filter(divisible_3, numbers))
print(new_list)