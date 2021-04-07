# Intro to Programming Using Python - Assignment #1
# Completed by:

# 1. Print out the following text:
# You've reached [your name].
print("You've reached Joe")
# I'm not available right now, so leave a message and I'll call you back.
print("I'm not available right now, so leave a message and I'll call you back.")

# 2. Create five variables for your first name, last name, shoe size, height, and age.
first_name = "Joe"
last_name = "Nomellini"
shoe_size = float(12.5)
height = '76"'
age = int(28)
# And then print them out on one line.
print(f"First Name: {first_name}, Last Name: {last_name}, Shoe Size: {shoe_size}, Height: {height}, Age: {age}")

# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount
# in a variable named total and print it out.

subtotal = float(10.58)
tip = float(0.22)

tip_amount = subtotal * tip

total = tip_amount + subtotal

print(f"Total Bill: {total:.2f}")

# 4. Convert 158.8 into an integer.
num = 158.8

print(int(158.8))


# Convert 75 into a float.

num2 = 75

print(float(75))
# Convert "244.9" into a float and then an integer.

print(float(244.9))

print(int(244.9))

# 5. Use \t and \n in a string and then print it out so that it matches (approximately) the following:
# -in the woods
print("-in the woods \n\t\twhich \n\t\t\tstutter \n\t\t\t\tand \n\n\t\t\t\t\tsting")
#               which
#                   stutter
#                           and
#
#                               sing

# 6. Put your first name and total from above into an f-string (f"...") so that it reads:
# Mattan, your total is $12.91
# (remember to round the total to the nearest cent)

print(f"Joe, your final bill is {total:.2f}")
# 7. Use input() to ask a user for the city they live in, and then print it back to them.
city = input("What city do you live in?")
print(city)

# 8. Build a future value calculator by using input() to get values from the user.
# (Make sure you convert them into integers or floats before doing any math on them.)
# Print out the result.
# Hint: Future Value = Present Value x (1 + rate of return) ^ number of periods

PV = float(input("Give me a number for present value."))
print(PV)

RoR = float(input("What rate of return would you like?"))
print(RoR)

N = int(input("For how many periods? Whole numbers only!"))
print(N)

FV = PV * ( 1 + RoR) ** N

print(FV)
