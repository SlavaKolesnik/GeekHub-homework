# 1. Write a script which accepts a sequence of
# comma-separated numbers from user and generates a
# list and a tuple with those numbers.
print('Введіть числа через кому:')

numbers = input()
list_numbers = numbers.split(',')
tuple_numbers = tuple(list_numbers)

print(list_numbers)
print(tuple_numbers)

# 2. Write a script which accepts two sequences of comma-separated
# colors from user. Then print out a set containing all the colors
# from color_list_1 which are not present in color_list_2.

color_list_1 = set(["yellow", "blue", "red", "green", "dark"])
color_list_2 = set(["orange", "red", "pink", "white", "black"])
a = 'список кольорів 1'
b = 'список кольорів 2'
print("В наявності є кольори:")
print(f'{a}:',color_list_1)
print(f'{b}:',color_list_2)
difference_list_1 = color_list_1.difference(color_list_2)
print(f'{a} відрізняється від {b}',difference_list_1)
difference_list_2 = color_list_2.difference(color_list_1)
print(f"{b} відрізніється від {a}",difference_list_2)

#3. Write a script which accepts a <number> from user and print
#out a sum of the first <number> positive integers.

m = 'введіть число:'
print(f'{m:.^30}')
x = int(input())
sum_number = sum(range(x+1))
print('сума числа:', x,'є:', sum_number)

# 4. Write a script which accepts a <number> from user and
# then <number> times asks user for string input. At the end
# script must print out result of concatenating all <number> strings.

text = 'Напишіть повідомлення:'
print(f'{text:-^30}')
massege = input()
print('Скільки разів написати ваше повідомлення?')
multiplication = eval(input('введіть ціле число:'))
res = massege * multiplication
print('Ваш результат:', res)

# 5. Write a script which accepts a decimal number from
# user and converts it to hexadecimal.

text = 'Введіть дестякове число:'
print(f'{text:.^30}')
decimal = eval(input())
number = int(decimal)
res = hex(number)
print('Ваше десткове число:',decimal, 'дорівнює шістнадцядтковому:', res)

# 6. Write a script to check whether a value from user input is
#         contained in a group of values.
#     e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#          [1, 2, 'u', 'a', 4, True] --> 5 --> False

text = 'введіть значення:'
print(f'{text:.^30}')
value = str(input())
if value in str([1, 2, 'u', 'a', 4, True, '&', '#$%']):
    True
    print(value, 'є в списку')
else:
    False
    print(value, 'нема в списку')

# 7. Write a script to concatenate all elements in
# a list into a string and print it. List must include
# both strings and integers and must be hardcoded.

my_list = ([1, 2, 4, True, 'Alabai', 'exodus', '@#@!#$$', False, 2.34, 66.1, 'J0$T0'])
res = "".join([str(_) for _ in my_list])
print(res)

