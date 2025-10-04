factor = 0
for count in range (2, 50):
	if 50 % count == 0:
		factor = factor + 1
		print(factor, count)