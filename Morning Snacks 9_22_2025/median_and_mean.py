number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))
number_4 = int(input("Enter forth number: "))

# computing sum
sum_of_numbers = number_1 + number_2 + number_3 + number_4
# computing for mean
mean = sum_of_numbers/4
# arranging in acsending order
acsending_1 = 0
acsending_2 = 0
acsending_3 = 0
acsending_4 = 0

#computing for median
# smalest number
if number_1 < number_2 and number_1 < number_3 and number_1 < number_4:
	acsending_1 = number_1
if number_2 < number_1 and number_2 < number_3 and number_2 < number_4:
	acsending_1 = number_2
if number_3 < number_2 and number_3 < number_1 and number_3 < number_4:
	acsending_1 = number_3
if number_4 < number_1 and number_4 < number_3 and number_4 < number_2:
	acsending_1 = number_4

#biggest number
if number_1 > number_2 and number_1 > number_3 and number_1 > number_4:
	acsending_4 = number_1
if number_2 > number_1 and number_2 > number_3 and number_2 > number_4:
	acsending_4 = number_2
if number_3 > number_2 and number_3 > number_1 and number_3 > number_4:
	acsending_4 = number_3
if number_4 > number_1 and number_4 > number_3 and number_4 > number_2:
	acsending_4 = number_4

#Second Biggest number
sum_of_highest_and_lowest = acsending_1 + acsending_4
sum_of_second_hihest_and_second_lowest = sum_of_numbers - sum_of_highest_and_lowest
median_of_numbers = sum_of_second_hihest_and_second_lowest/2

print("Sum of numbers is: ", sum_of_numbers)
print("Mean of numbers is: ", mean)
print("smallest numner is : ", acsending_1)
print("biggest numner is : ", acsending_4)
print("Median of numbers is: ", median_of_numbers)