# sets remove duplicates - can pop -- they are unordered hence no last element
numbers = [1, 2, 6, 3, 1, 1, 6]
uniques_nums = set(numbers)
print(uniques_nums)

# Sets support the in operator the same as lists do.
# You can add elements to sets using the add method, and remove elements using the pop method, similar to lists.
# Although, when you pop an element from a set, a random element is removed.
# Remember that sets, unlike lists, are unordered so there is no "last element".
fruit = {"apple", "banana", "orange", "grapefruit"}  # define set
print("watermelon" in fruit)
print(type(fruit))

# add element to a set
fruit.add("watermelon")
print(fruit)

# pop an element in set
print(fruit.pop())
print(fruit)

