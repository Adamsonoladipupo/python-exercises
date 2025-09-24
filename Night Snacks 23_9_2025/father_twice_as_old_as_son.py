"""
Pseudocode:
- write a prompt highlighting the use of the app to the user
- declare and initialize a variables that store an input from the user as the:
 	- current year
	- father's current age
	- son's current age
- declare a variable that store the value of when the father is/was twice as old as the son, and initialize it to be 2 multiply by the son's age minus the father's age
- declare a variable that store the year when the father is/was twice as old as the son, initilize it to be currenct year plus the father's twice as old age
- print the number of years ago the father is/was twice as old as the son and the year. 

"""

print("Welcome! This app helps you determine the number of years and year you are twice as old as your son")
current_year = int(input("Enter the current year: "))
father_current_age = int(input("Enter the father's currecnt age: "))
son_current_age = int(input("Enter the son's current age: "))
father_twice_as_old = 2*son_current_age - father_current_age
year_father_twice_as_old = current_year + father_twice_as_old
print("Father was/is twice as old as son ",father_twice_as_old ,"years ago, in the year ", year_father_twice_as_old,".")