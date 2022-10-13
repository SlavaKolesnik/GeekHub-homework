# 1. Write a script that will run through a list of tuples and replace
# the last value for each tuple. The list of tuples can be hardcoded.
# The "replacement" value is entered by user. The number of elements
# n the tuples must be different.


list_tuple = [(13, 21, 32), ('Sakura', 'Pego', 'Qwerty'), (2.52, 124.456, 1234.345), ()]
m = input('Enther something:\n')
spare_list = []


for i in range(len(spare_list)):
    new_items = list(list_tuple[i])
    new_items[-1] = m
    list_tuple[i] = tuple(new_items)


print(list_tuple)
