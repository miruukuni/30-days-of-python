# fname = "John"
# lname = "Doe"
# fullname = fname + " " + lname
# country = "USA"
# city = "New York"
# age, year, is_married, is_true, is_light_on = 24, 2020, False, True, True


# print(type(fullname), 'is the name')
# print(len(fullname) - 1, 'is the length of the name')

# if len(fname) > len(lname):
#     islonger = True
# elif len(fname) < len(lname):
#     islonger = False
# else:
#     islonger = 'equal'
# print(islonger, 'is the result')

num_one = 16
num_two = 2

print(num_one)

num_after = num_one + num_two

num_afterafter = num_one / num_two


print(int(num_afterafter))

import math

radius = 10
area = math.pi * radius ** 2
print(area)

print(1 == 1)

# Two separate lists with the same numbers
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True  (The numbers inside are the same)
print(a is b)  # False (They are different lists in memory)


if a == b and a is not b:
    print("The lists are equal but not the same object in memory.")
elif a == b or a is b:
    print("The lists are either equal or the same object in memory.")
elif not a == b and not a is b:
    print("The lists are neither equal nor the same object in memory.")
