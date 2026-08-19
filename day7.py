# # syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# st.add('item5')
# print(st)

# random_removed = st.pop()
# print(random_removed)
# removed = st.remove('item3')

# print(st)

# st.add('item6')
# st.update({'item7', 'item8'})
# print(st)

# st_2 = {'item1', 'item2', 'item3', 'item4', 'item6'}
# st_3 = {'item1', 'item2', 'item3', 'item4', 'item5', 'item7'}

# st2 = st_2.difference(st_3)
# print(st2)
# st3 = st_3.difference(st_2)
# print(st3)
# st2 = st_2.symmetric_difference(st_3)
# print(st2)

# st3 = st_2.intersection(st_3)
# print(st3)

# # .issubset() and .issuperset()

# st4 = {'item7', 'item8', 'item9'}
# print(st4.isdisjoint(st_2), st4.isdisjoint(st_3))


                                        #Exercise 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['LinkedIn', 'Snapchat'])
it_companies.remove('IBM')

#discard doesn't show any error if the item that was supposed to get remove() doesn't exist

                                        #Exercise 2
print(B.difference(A))
print(B.symmetric_difference(A))

ab = A.union(B)
print(A)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
A.update(B)
B.update(A)
print(B.symmetric_difference(A))
del A
del B
del ab

                                        #Exercise 3
agest = set(age)
print(len(agest) > len(age))
print(len(agest))
print(len(age))

#string is a single value, list is multiple values in order and will take repeated values, tuple is a list that can't be modified, set is a list that can't have repeated values and is unordered
text = 'I am a teacher and I love to inspire and teach people'
text = text.split()
text = set(text)
print(len(text))