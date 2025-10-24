temperatures = [0, 20, 37, 100]
def to_fahrenheit(input):
	return input* 1.8 + 32
fahrenheit = list(map(to_fahrenheit, temperatures))
print (fahrenheit)