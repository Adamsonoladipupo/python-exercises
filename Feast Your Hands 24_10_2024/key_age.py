dictionary = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]

def key_age(input):
	return input["age"] > 25

age_greater_than_25 = list(filter(key_age, dictionary))
print(age_greater_than_25)