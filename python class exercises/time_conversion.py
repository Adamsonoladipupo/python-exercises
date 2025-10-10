def time_conversion(user_input):
	hour = user_input / 60
	second = user_input * 60
	return hour, second

user_input = int(input("Enter your time in minutes: "))
result = time_conversion(user_input)
print(f"{user_input}min is {result}hour and sec respectively")
	