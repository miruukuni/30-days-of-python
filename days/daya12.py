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


