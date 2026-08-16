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

fruits.append('add something here') #adds permanently to the end of the list
print(fruits)
fruits.insert(2, 'add something here2')
fruits.extend(lst)  # adds an item to the end of the list
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'add something here', 'add something here2']
fruits.remove('mango')  #has to remove the entire thing?
print(fruits) 
fruits.pop(4)
print(fruits)

del fruits[:-1] #or just 'del fruits' to get rid of everything
print(fruits)

fruits.clear()
print(fruits)

copy_lis = lst.copy() #go wild with experiments on copy_lis, does not affect lst

print(lst.count('ite'))
print(lst.count('item1')) 

#.find to find the index number

#.reverse reverses the list, same thing as [::-1]?

#.sort sorts to alphabetical order, add reverse=True inside argument to make it reverse alphabetical

