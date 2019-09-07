# concatenation
first = "Hello"
second = "World!"
print(first + " " + second)

# ' and "
salesman = '"I think you\'re an encyclopedia salesman"'
print(salesman)

# single '
string = 'Simon\'s skateboard is in the garage'
print(string)

# multiply
print((first + " ") * 5)

# get length - len doesnt work with numbers - object int has no method len
length = len("Udacity")
print("Udacity has " + str(length) + " characters")

# string indexing
print("Hello"[0])

course = "Python for Beginners"

# prints the last character
print(course[-1])

# print 0 , 1, 2 but excludes the 3
print(course[0:3])

# without index - starts from 0
print(course[:5])

# print all
print(course[:])

name = "Jennifer"
print(name[1:-1])

first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a coder'
print(msg)

# check a string exists in
print("Python" in course)
