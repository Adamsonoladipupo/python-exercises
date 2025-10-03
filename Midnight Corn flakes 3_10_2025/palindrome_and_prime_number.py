def palindrome_and_prime_number(a):

	unith = 0
	tenth = 0
	hundredth = 0

	if a % 10 != 0 or a // 10 != 0:
		unith = a % 10
		a = a // 10
	if a % 10 != 0 or a // 10 != 0:
		tenth = a % 10
		a = a // 10
	if a % 10 != 0 or a // 10 != 0:
		a = a % 10
		hundredth = a // 10

	if unith == hundredth:
		return print("Palindromes")
	else:
		return print("Not a Palindromes")


number = int(input("Enter a number: "))
check = palindrome_and_prime_number(number)