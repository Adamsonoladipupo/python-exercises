"""
Pseudocode
- write a prompt highlighting the use of the app to the user
- Collect three inputs from the user, store them each in a variable as score1, score2 and score3.
- declare and initialize a variable as the average of the scores, initialize it to be the sum of the three score, and divide it by 3.
- check if the average is less than equals to 100 and greater than equals to 90, print "A", if not,
- check if the average is less than 90 and greater than equals to 80, print "B", if not,
- check if the average is less than 80 and greater than equal to 70, print "C", if not
- check if the average is less than 70 and greater than equal to 60, print "D", if not
- print "F"

"""
print("Welcome! This app helps you grade a student based on their score")
score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))
average_score = (score1+score2+score3)/3
if 90<= average_score <=100:
	print("your grade is A")
elif 80<= average_score <90:
	print("your grade is B")
elif 70<= average_score <80:
	print("your grade is C")
elif 60<= average_score <70:
	print("your grade is D")
elif 0<= average_score <60:
	print("your grade is F")
else:
	print("INVALID result, not within the scope of the grading system")
