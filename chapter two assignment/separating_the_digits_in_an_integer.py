user_input = int(input("Enter a 5digits number: "))
unit = 0
tenth = 0
hundredth = 0
thousandth = 0
tenth_thousand = 0
if user_input % 10 != 0 or user_input // 10 != 0:
	unit = user_input % 10
	user_input = user_input // 10
if user_input % 10 != 0 or user_input // 10 != 0:
	tenth = user_input % 10
	user_input = user_input // 10
if user_input % 10 != 0 or user_input // 10 != 0:
	hundredth = user_input % 10
	user_input = user_input // 10
if user_input % 10 != 0 or user_input // 10 != 0:
	thousandth = user_input % 10
	tenth_thousand = user_input // 10

print(tenth_thousand, "  ",thousandth, "  ",hundredth, "  ", tenth, "  ",unit )
