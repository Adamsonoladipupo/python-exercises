
docstring = """
	Using this formula 
	P = P0 x e^rt
	P = total pupolation after time t
	P0 = starting population = 8231970628 at 2025
	r = % rate of growth = 0.85 per year
	T = time in hour of the day
	e = Euler number = 2.71818
	
"""
print(docstring)
population = 1
time = 1
for time in range (1, 101):
	population = 8231970628 * (2.71818**(0.85*time))
	increase = population - (8231970628 * (2.71818**(0.85*(time-1))))
	
	print(time,"          ", population, "          ", increase)
#print("Year")
	