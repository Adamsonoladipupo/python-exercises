new_collection = {1,2,3,4,5}

def remove_item(collection, item):
    if item in collection:
        collection.remove(item)
        return item
    else:
        return "none"
    return none
print(remove_item(new_collection, 8))