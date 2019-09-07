while True:
    try:
        x = int(input("Please enter a number: "))
        print("Number is " + str(x))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

age = 14
is_teen = 12 < age < 20
print(is_teen)