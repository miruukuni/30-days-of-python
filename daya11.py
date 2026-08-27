import math


def add_two_numbers(a, b):
    return a + b

a = input("Enter first number: ")
b = input("Enter second number: ")
print(add_two_numbers(int(a), int(b)))

def area_of_circle(r):
    return math.pi * r * r

def add_all_numerbers(*args):   #make it add an infinite amount of number until state otherwise,        while loop
    
    return sum(args)

def convert_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

def check_month(month):                     #add a function to make it so lowerrcase works
    month = month.lower()
    if month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    elif month in ["september", "october", "november"]:
        return "Fall"
    else:
        print("try again")

print(check_month("January"))

def calculate_slope():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    
    slope = (y2 - y1) / (x2 - x1)
    return slope

