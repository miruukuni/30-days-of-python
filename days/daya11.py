import math
from unicodedata import name


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

def printlist(lst):
    for i in lst:
        print(i)

lst = [1, 2, 3, 4, 5]
otherlst = ["apple", "banana", "cherry"]
printlist(lst)

def reverselist(lst):
    return lst[::-1]

reverselist(lst)

def capitalize_list_item(lst):
    return [item.upper() for item in lst]

print(capitalize_list_item(otherlst))

def add_item_to_list(lst, item):
    lst.append(item)
    return lst

def remove_item_from_list(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_numbers(number):
    total = 0
    for i in range(1, number + 1):
        total += i
    return total

print(sum_of_numbers(5))

def sum_of_odds(number):
    total = 0
    for i in range(1, number + 1):
        if i % 2 == 1:
            total += i
    return total

def sum_of_evens(number):
    total = 0
    for i in range(1, number + 1):
        if i % 2 == 0:
            total += i
    return total




# ----------------------------------------------------------------------------------------------

def evens_and_odds(number):
    odd_count = 0
    even_count = 0
    for i in range(0, number+1):
        if i % 2 == 1:
            odd_count += 1
        elif i % 2 == 0:
            even_count += 1
        print(i)
    odd_even = (f"number of odds are {odd_count}, number of even are {even_count}")
    return odd_even

print(evens_and_odds(100))


def factorial(number):
    return math.factorial(number)

factorial(5)

def is_empty(lst):
    if len(lst) == 0 or lst == []:
        return True
    else:
        return False

def calculate_mean(number):
    default = 0
    for i in number:
        default += i
    return default / len(number)

def calculate_mean_other(number):
    return sum(number) / len(number)

calculate_mean([1, 2, 3, 4, 5])


def greet(fname = "Guest"):
    print(f"Hello, {fname}!")

def show_args(*args):
    for arg in args:
        print(arg)




#--------------------------------------------------------------------------------------------------------

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):     #i understand the code but i have absolutely no clue the thought process behind how to filter out prime numbers
        if num % i == 0:
            return False
    return True

def is_unqiue(lst):
    return len(lst) == len(set(lst))

def is_unique_other(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True

import infos_to_import.info_countries as info_countries
""""Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order."""
#day 10 ptsd