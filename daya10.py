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

print(len(unique_languages))

all_languages = []
for i in countries_info:
    all_languages.extend(i['languages'])

for i in all_languages:
    # print(f"{i}: {all_languages.count(i)}")

    top = [all_languages.count(i)]
    top.sort()

    # print(all_languages.count(i))
    # if top > 5:
    #     print(f"{i}: {all_languages.count(i)}")
    

# all_languages.sort()
# print(all_languages)