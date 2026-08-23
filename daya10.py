# # for i in range(0, 11):
# #     print(i)

# # for i in range(11, 0, -1):
# #     print(i)

# for i in range(0,7):
#     print('#' * (i + 1))

# for i in range(0, 8):
#     print(' ' * (7 - i) + '#' * (i + 1))

# for i in range(0, 8):
#     print('# ' * 8)

# for i in range(0,10):
#     print(f"{i} * {i} = {i * i}")


# words = ['Python', 'Numpy','Pandas','Django', 'Flask']

# for i in range (0, len(words)):
#     print(words[0+i])

# for i in range (0, 101, 2):
#     print(i)

# for i in range (0, 101):
#     if i % 2 != 0:
#         print(i)
# for i in range (0, 101):
#     print(i, 'Even' if i % 2 == 0 else 'Odd')

# def trigger(): 
#     for i in range (0, 101):
#         print(i)


#                         #exercise 2
# for i in range (0, 101):
#     print(i)
# print(sum(i for i in range (0, 101)))

# print(sum(i for i in range (0, 101) if i % 2 == 0))
# print(sum(i for i in range (0, 101) if i % 2 != 0))


                        #exericse 3
import countries

countries = countries.countries

                # for i in range(0, len(countries)):
                #     countries = str(countries)
                #     if 'land' in countries:
                #         print(i)
                # print(countries if 'land' in countries else 'recheck code')

# for i in countries:     #i understand it now.
#     if 'land' in i:
#         print(i)

# fruit = ['banana', 'orange', 'mango', 'lemon']
# for i in fruit[::-1]:
#     print(i)


                #HUGE
import info_countries

countries_info = info_countries.infocountries


unique_languages = set()

for i in countries_info:
    unique_languages.update(i['languages'])

print(f"total amount of languages: {len(unique_languages)}")

print('-----------------------------------')        #the worst coding session of my life

all_languages = []
for i in countries_info:
    all_languages.extend(i['languages'])

# print(set(all_languages))
# print(len(set(all_languages)))


count_per_language = []
for i in set(all_languages):
    count = all_languages.count(i)
    count_per_language.append((i, count))

# print(count_per_language)
count_per_language.sort(key=lambda x: x[1], reverse=True)
# print(count_per_language)

print('top 10 most spoken languages:')
for i, count in count_per_language[:10]:
    print(f"{i}: {count}")
                #took 7 attempts, I WILL DESTROY THIS ENTIRE WORLD


    # print(f"{i}: {all_languages.count(i)}")
    # count = all_languages.count(i)
    # count_per_language = {i: count}
    # print(count_per_language)
    # count_per_language.sort(key=lambda x: x[1], reverse=True)


    # print(f"{i}: {all_languages.count(i)}")

    # top = [all_languages.count(i)]
    # top.sort()

    # print(all_languages.count(i))
    # if top > 5:
    #     print(f"{i}: {all_languages.count(i)}")
    

# all_languages.sort()
# print(all_languages)


#THE CODE DONT CODE

'''
lesson 1:
don't put everything inside a loop

lesson 2:
for (variable) in (variable2):
variable2 is getting iterated literally, and whatever value it gets to get assigned to variable1

lesson 3:
coding is hard, lockin leetcode

'''

print('-----------------------------------')

country_population = []
for i in countries_info:
    country_population.append((i['name'], i['population']))
country_population.sort(key=lambda x: x[1], reverse=True)

print('top 10 most populated countries:')
print(country_population[:10])

#brains are fried but atleast im done