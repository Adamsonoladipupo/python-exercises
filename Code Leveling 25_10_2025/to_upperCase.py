words = ['python', 'java', 'c++']

def to_upper(inputs):
	return inputs.upper()

new_list = list(map(to_upper, words))
print(new_list)