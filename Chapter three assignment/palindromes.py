user_input = int(input("Enter a five digits number: "))
unith = 0
tenth = 0
hundredth = 0
thousandth = 0
tenththousand = 0

if user_input % 10 != 0 or user_input // 10 != 0:
	unith = user_input % 10
	user_input = user_input // 10
if user_input % 10 != 0 or user_input // 10 != 0:
	tenth = user_input % 10
	user_input = user_input // 10
if user_input % 10 != 0 or user_input // 10 != 0:
	hundredth = user_input % 10
	user_input = user_input // 10
if user_input % 10 != 0 or user_input // 10 != 0:
	thousandth = user_input % 10
	tenththousand = user_input // 10



if unith == tenththousand and tenth == thousandth:
	print("Yes, this is a Palindromes")
else:
	print("Not a Palindromes")
