#gallons = int(input("Enter the gallons used (-1 to end): "))
gallons = 1;
miles = 1
sum_of_gallon = 0
sum_of_miles = 0
while gallons != -1:
	gallons = int(input("Enter the gallons used (-1 to end): "))
	miles = int(input("Enter the miles driven: "))
	sum_of_gallon += gallons
	sum_of_miles += miles
	miles_per_gallon = miles/ gallons
	print(f"the miles per gallon for this trip was: {miles_per_gallon}") 
overall_average = sum_of_miles/sum_of_gallon
print(f"The overall average miles/gallon was: {overall_average}")