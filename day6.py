empty = ()
siblings = ('Josh', 'Emily')
print(len(siblings))
parents = ('John', 'Jane')
family_members = siblings + parents

brother, sister, father, mother = family_members

fruits = ('apple', 'orange', 'banana')
vegetables = ('carrot', 'potato', 'onion')
animal_products = ('milk', 'beef', 'pork')

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lit = list(food_stuff_tp)

print(food_stuff_tp)
middle_item = food_stuff_lit[len(food_stuff_lit) // 2]
print(middle_item)

print(food_stuff_lit[0:3] + food_stuff_lit[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)