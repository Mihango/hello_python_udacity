num = 13.0
print(type(num))

# convert num to str
print(str(num))

# convert string to float or int
num2 = float("34.0")
num3 = int("12")

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

# Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
print("This week\'s total sales: " + str(int(mon_sales) + int(tues_sales) + int(wed_sales)
                                          + int(thurs_sales) + int(fri_sales)))
