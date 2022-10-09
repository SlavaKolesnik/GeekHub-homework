# 1. Write a script which accepts a sequence of
# comma-separated numbers from user and generates a
# list and a tuple with those numbers.
print('Введіть числа через кому:')

numbers = input()
list_numbers = numbers.split(',')
tuple_numbers = tuple(list_numbers)

print(list_numbers)
print(tuple_numbers)
