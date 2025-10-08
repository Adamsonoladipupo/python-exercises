user_input = int(input("Enter a Polindrome number: "))
#initial_user_input 
user_input = user_input_v2 = user_input
digit_count = 1
while user_input > 9:
	single_number = user_input % 10
	user_input = user_input // 10
	digit_count = digit_count + 1

single_digit = 0
palindromes = 0
user_input_v2 = user_input_v3 = user_input_v2
for count in range (digit_count, 0, -1):
	single_digit = user_input_v2 % 10
	user_input_v2 = user_input_v2 // 10
	palindrome = single_digit * (10 ** (count-1))
	palindromes = palindromes + palindrome

if user_input_v3 == palindromes:
	print("Yes, this is a Polindrome")
else:
	print("This is not a Polindrome")
	