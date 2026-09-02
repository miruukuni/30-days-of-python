# # some = 'what'

# # why = input('can you' + some)

# # print(why)


# # number = (input('Enter a number: '))

# # # if number == 67:
# # #     print('SIX SEVEN SIX SEVEN SIX SEVEN SIX SEVEN')
# # # elif number == 69:
# # #     print('you naughty little')
# # # elif not isinstance(number, int):
# # #     print('youre wrong')
# # # else:
# # #     print(number)


# # if number.isdigit():
# #     number = int(number)
# #     if number == 67:
# #         print('SIX SEVEN SIX SEVEN SIX SEVEN SIX SEVEN')
# #     elif number == 69:
# #         print('you naughty little')
# #     else:
# #         print(number)
# # else:
# #     print('youre wrong')

    
# # print(type(number))

# user_input = "hello"

# # ❌ The old, messy way:
# print("'" + user_input + "' is not a valid number!")

# #  The clean f-string way:
# print(f"'{user_input}' is not a valid number!")



# user_input = input('Enter a number: ')

# try:
#     # Try to convert it to an integer
#     number = int(user_input)
    
#     if number == 67:
#         print('SIX SEVEN SIX SEVEN SIX SEVEN SIX SEVEN')
#     elif number == 69:
#         print('you naughty little')
#     else:
#         print(number)

# except ValueError:
#     # This runs ONLY if int() failed (e.g., they typed letters)
#     print(f"'{user_input}' is not a valid number!")


num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
if num_str == str(num_int):
    print(f'num_str: {num_str}')