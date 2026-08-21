# # # #                     #no.1

# # # # # # age = input('enter your age: ')

# # # # # # if not age.isdigit():           #for loop
# # # # # #     print('put actual age')
# # # # # # else:           #should separate the verification and the rest
# # # # # #     age = int(age) - 18
# # # # # #     if age >= 0:
# # # # # #         print('you are old enough to drive')
# # # # # #     else:
# # # # # #         print(f"you need {abs(age)} more years to drive")


# # # # #                     #no.2
# # # # # my_age = 18

# # # # # is_answered = False

# # # # # while is_answered == False:
# # # # #     age = input('enter your age: ')
# # # # #     if not age.isdigit():
# # # # #         print('put actual age')
# # # # #         is_answered = False
# # # # #     else:
# # # # #         age = int(age)
# # # # #         is_answered = True

# # # # # if age > my_age:
# # # # #     print(f"you are {age - my_age} years older than me")
# # # # # elif age < my_age:
# # # # #     print(f"you are {my_age - age} years younger than me")
# # # # # else:
# # # # #     print('we are the same age')


# # # #                     #no.3
# # # # a = int(input('enter a number: '))
# # # # b = int(input('enter another number: '))

# # # # if a > b:
# # # #     print(f"{a} is greater than {b}")
# # # # elif a < b:
# # # #     print(f"{a} is smaller than {b}")
# # # # else:
# # # #     print(f"{a} is equal to {b}")

# # #                     #no.4
# # # score = int(input('enter score: '))
# # # grade = {0<=score<=59: 'F', 60<=score<=69: 'D', 70<=score<=79: 'C', 80<=score<=89: 'B', 90<=score<=100: 'A'}

# # # print(grade[True])

# # # score = int(input('enter score: '))           #if statement is more efficient?
# # # if score <= 59:
# # #     print('F')
# # # elif score <= 69:
# # #     print('D')
# # # elif score <= 79:
# # #     print('C')
# # # elif score <= 89:
# # #     print('B')
# # # elif score <= 100:
# # #     print('A')
# # # else:
# # #     print('Invalid score')

# #                     #no.5
# # enter_month = input('enter month: ').lower()
# # if enter_month in ['september', 'october', 'november']:
# #     print('the season is Autumn')
# # elif enter_month in ['december', 'january', 'february']:
# #     print('the season is Winter')
# # elif enter_month in ['march', 'april', 'may']:
# #     print('the season is Spring')
# # elif enter_month in ['june', 'july', 'august']:
# #     print('the season is Summer')
# # else:
# #     print('Invalid month')

#                     #no.6
# fruits = ['banana', 'orange', 'mango', 'lemon']         #sets are probably better

# added_fruit = input('enter a fruit: ').lower()
# if added_fruit in fruits:
#     print('that fruit already exists in the list')
# else:
#     fruits.append(added_fruit)
#     print(fruits)

                    #no.7
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

keyword = input('what do you want to check for? ').lower()


if not keyword in person:
    print('data not in dictionary')
elif keyword == 'skills':
    skills = person['skills']
    print(f"middle skill: {skills[len(skills) // 2]}")

    if 'Python' in skills:
        print('Python is in the skills')

    if set(skills) == {'Javascript', 'React'}:
        print('frontend dev')
    elif set(skills) == {'Node', 'Python', 'MongoDB'}:
        print('backend dev')
    elif set(skills) == {'React', 'Node', 'MongoDB'}:
        print('fullstack dev')
    else:
        print('unknown title')

#not sure if requirement ask for ONLY having those skills or having atleast those skills to be given a title
    if set(skills) == {'Javascript', 'React'}:
        print('frontend dev')
    elif set(skills) == {'Node', 'Python', 'MongoDB'}:
        print('backend dev')
    elif 'React' and 'Node' and 'MongoDB' in skills:
        print('fullstack dev')
    else:
        print('unknown title')

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")


#such a long session