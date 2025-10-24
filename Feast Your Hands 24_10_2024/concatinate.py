from functools import reduce

message = ["Hello", " ", "World"]
def concatinate(input, inputs):
	return input + " " + inputs

new_message = reduce(concatinate, message)
print(new_message)