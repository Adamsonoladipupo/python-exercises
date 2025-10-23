words = ["apple", "banana", "cherry"]

def strings_length(words):
	return len(words)

string_len = list(map(strings_length, words))
print(string_len)