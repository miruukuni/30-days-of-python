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

                                        #exercise 1:
empty = []

five_more = [1, 2, 3, 4, 5]

print(len(five_more))

print(five_more[0:5:2])

mixed_data_types = ['troy', 18, 5.9, 'single', 'US']
name, age, height, status, country = mixed_data_types

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)

print(len(it_companies))

print(it_companies[0:7:3])

it_companies[4] = 'extra company '
print(it_companies)

it_companies.insert(3, 'IT company')

print(len(it_companies))
print(it_companies)

it_companies.insert(4, 'middle company')

print(it_companies)

it_companies[4] = it_companies[4].upper()
print(it_companies)
print(it_companies[3].upper())

it_companies = it_companies + ['#: ']
print(it_companies)

print('small' in it_companies)

it_companies.sort(reverse=True)
print(it_companies)
it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

sliced_it_companies = it_companies[:3]
print(sliced_it_companies)
other_sliced = it_companies[-3:]
print(other_sliced)

print(len(it_companies))
middle_slice = it_companies[3:6]
print(middle_slice)
print(it_companies)
it_companies.remove('extra company ')
print(it_companies)
it_companies.remove(it_companies[int((len(it_companies) - 1) // 2)])
print(it_companies)
it_companies.remove(it_companies[len(it_companies) - 1])
print(it_companies)
it_companies.clear()
print(it_companies)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined = front_end + back_end
print(joined)

full_stack = joined.copy()
full_stack.insert(0, 'Python')
full_stack.insert(1, 'SQL')
print(full_stack)

                                            #exercise 2:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print(ages[0], ages[-1])
median = ages[len(ages) // 2]
print(median)
average = sum(ages) // len(ages)
print(average)
ranges = ages[-1] - ages[0]
print(ranges)

print(abs(ages[0]-average) > abs(ages[-1]-average))

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 
             'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 
             'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 
             'Dominican Republic', 'East Timor (Timor-Leste)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 
             'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 
             'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 
             'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 
             'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 
             'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 
             'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 
             'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 
             'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

print(countries[len(countries) // 2])
first_half = countries[:len(countries) // 2]
print(first_half)
second_half = countries[len(countries) // 2:]
print(second_half)

these_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_coun, second_coun, third_coun, *scandic_coun = these_countries
print(first_coun)
print(second_coun)
print(third_coun)
print(scandic_coun)