birth_year = input("What is your birth year? ")

try:
    age = 2019 - int(birth_year)
    print(age)
except ValueError:
    print("Your entered wrong number")
