# lists are mutable while string are immutable
list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0])

# index not available throws IndexError
try:
    list_of_random_things[5]
except IndexError:
    print("Index Error Occurred")

# last element
print(f"Last element >>>>>> {list_of_random_things[-1]}")
print(f"Last 3 element >>>>>> {list_of_random_things[-3]}")

# membership operator - in and not in
print(f"is 1 in list {1 in list_of_random_things}")

print(f"is 2 not in list {2 in list_of_random_things}")

# slicing
print(list_of_random_things[1:2])
print(list_of_random_things[:2])

sentence1 = "I wish to register a complaint."
print(len(sentence1))

sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]
sentence2[0:2] = ["We", "Want"]
print(sentence2)

# add item to list
list2 = [0]
print(list2)
list2.append(23)
print(list2)

print(max([1, 23, 4, 34, 100]))
print(min([1, 23, 4, 34, 100]))
print(sorted([1, 23, 4, 34, 100]))
