first_score = int(input("Enter the first score: "))
second_score = int(input("Enter the second score: "))
third_score = int(input("Enter the third score: "))

highest_score = first_score
if second_score > highest_score :
	highest_score = second_score
if third_score > highest_score :
	highest_score = third_score
print("The highest score is: ", highest_score)