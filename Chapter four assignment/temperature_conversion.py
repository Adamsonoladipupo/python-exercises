def to_fahrenheit(celcius):
	fahrenheit = (9 * celcius)/5 + 32
	return fahrenheit

temperature = int(input("Enter your reading: "))
result = to_fahrenheit(temperature)
print(result)