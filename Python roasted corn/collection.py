
collection = set()
for repeat_10x in range(0,10):
    user_input = int(input("Enter a number: "))
    collection.add(user_input)
print(collection)

def sum_collection(collection):
    total = 0
    for item in collection:
        total += item
    return total
print(sum_collection(collection))