set_one = {1,2,3,4,5}
set_two = {4,5,6,7,8}

def find_intersection(set_one, set_two):
    new_set = set_one & set_two
    return new_set

print(find_intersection(set_one, set_two))

def unite_set(set_one, set_two):
    new_set = set_one | set_two
    return new_set

print(unite_set(set_one, set_two))

def remove_all_elements_in_set_one(set_one, set_two):
    set_one.clear()
    return set_one, set_two
print(remove_all_elements_in_set_one(set_one, set_two))