# lis = ['one', 'two', 'three', 'four']

# print('lis:', lis)
# print('Number of items:', len(lis))

# print(lis[2])

lst = ['item1','item2','item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10']
first_item, *second_item, third_item, rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

print('-------------------')

first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

fruits = ['banana', 'orange', 'mango', 'lemon']
what = fruits[::-1]
print(what)  # ['lemon', 'mango', 'orange', 'banana']
something = fruits[::-2]
print(something)  # ['lemon', 'orange']
orange_and_lemon = fruits[::2]
print(orange_and_lemon)  # ['banana', 'mango']
huh = fruits[:1]                         #takes the 0th index because it ends at the first index
print(huh)  # ['banana']
heh = fruits[:-1]                        #ignores the last index and takes everything else
print(heh)  # ['banana', 'orange', 'mango']

