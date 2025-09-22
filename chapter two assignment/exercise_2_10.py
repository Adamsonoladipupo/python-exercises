print("Enter three integers")
number_1 = int(input("First number: "))
number_2 = int(input("Second number: "))
number_3 = int(input("Third number: "))
sum = number_1 + number_2 + number_3


print("Sum of numbers is: ",sum)
print("Product of numbers is: ", number_1*number_2*number_3)
print("Smallest number is: ", min(number_1, number_2, number_3))
print("Largest number is: ", max(number_1, number_2, number_3))
print("Average of numbers: ", sum/3)