def rounding_numbers(float, digits = None):
	if digits == 0:
		result = round(float, digits)
		result = int(result)
		return result
	result = round(float, digits)
	return result


docstring = """

	Welcome this app helps you round floats,
	Enter a float and the digits you are rounding to.
	
	1 --> tenth
	2 --> hundredth
	3 --> thousandth
	0 --> whole number	
	
"""
print(docstring)
float_input = float(input("Enter a float number: "))
digits = int(input("Enter digits: "))
rounded = rounding_numbers(float_input, digits)
print(rounded)
