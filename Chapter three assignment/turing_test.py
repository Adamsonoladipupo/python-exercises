first_user_prompt = input("What is your problem?: ")
second_user_prompt = input("Have you had this problem before (yes or no)?: ")
if second_user_prompt == "yes":
	print("print 'Well, you have it again.")
elif second_user_prompt == "no":
	print("Well, you have it now.")

docstring = """
	No, this conversation will not convince the user
	that the entity at the other end exhibited
	intelligent behavior, because the entity could not
	understand the problem by providing a solution to
	the problem.
"""
print(docstring)