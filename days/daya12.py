import string
import random

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(random_user_id())

def user_id_gen_by_user():
	for i in range(int(ids)):
		the_ids = ''.join(random.choices(string.ascii_letters + string.digits, k=characters))
		yield the_ids

characters = int(input("how long"))
ids = input("how maany")

for i in user_id_gen_by_user():
    print(i)

def rgb_color_gen():
    first = random.randint(0, 255)
    second = random.randint(0, 255)
    third = random.randint(0,255)
    full = f"rgb({first}, {second}, {third})"
    return full

print(rgb_color_gen())


#------------------------------------------------------------------------------------------------

def list_of_hexa_color():
    return '#' + ''.join(random.choices(string.ascii_letters[0:6] + string.digits[0:9], k=6))

print(list_of_hexa_color())

def list_of_rgb_color():
    first = random.randint(0, 255)
    second = random.randint(0, 255)
    third = random.randint(0,255)
    full = f"rgb({first}, {second}, {third})"
    return full

def generate_colors(type, amount):
    if type == "hex":
        for _ in range(amount):
            print(list_of_hexa_color())
    elif type == "rgb":
        for _ in range(amount):
            print(list_of_rgb_color())

generate_colors("rgb", 5)


#----------------------------------------------------------------

a = ["Math", "English", "Programming", "Physics", "Music"]

def shuffle_list(a):
    random.shuffle(a)
    return a

def seven_random_number():
     a = set()
     seven_numbers = False
     while seven_numbers == False:
         a.add(random.choice(string.digits[0:9]))
         if len(a) >= 7:
             seven_numbers = True
     return list(a)

print(seven_random_number())