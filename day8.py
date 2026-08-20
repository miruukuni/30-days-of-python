something = {'a' : 1, 'b': 2, 'c': 3, 'e': 5}
something['d'] = 4

something['b'] = 5

print(something['b'])

something.pop('c')
something.popitem()
del something['a']

print(something)
print(something.items())

something.clear()
del something

#.copy

reborn = {'a' : 1, 'b': 2, 'c': 3, 'e': 5}

print(reborn.keys())
print(reborn.values())

                                                #Exercise
dog ={}
dog['name'], dog['color'], dog['breed'], dog['legs'], dog['age'] = 'doggy', 'black', 'random', '4', '10'

student = {'first_name': 'John', 
           'last_name': 'Doe', 
           'gender': 'male', 
           'age': 25, 
           'marital_status': 'single', 
           'skills': ['Python', 'JavaScript'], 
           'country': 'USA', 
           'city': 'New York', 
           'address': {'street': '123 Main St', 'zip_code': '10001'}
           }

print(len(student))

print(student['skills'])
print(type(student['skills']))

student['skills'].append('teaching')
student['skills'].append('running')
print(student['skills'])

print(student.keys())
print(student.values())

print(student.items())

del student['first_name']

del student