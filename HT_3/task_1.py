# 1. Write a script that will run through a list of tuples and replace
# the last value for each tuple. The list of tuples can be hardcoded.
# The "replacement" value is entered by user. The number of elements
# n the tuples must be different.

list_tuple = [(13, 21, 32), ('Sakura', 'Pego', 'Qwerty'), (2.52, 124.456, 1234.345)]
lst, lst1, lst2 = [*list_tuple[0]], [*list_tuple[1]], [*list_tuple[2]]
x = input('Enter something:\n')


for l in lst, lst1, lst2:
    del l[-1]
    l.append(x)


tpl, tpl1, tpl2 = tuple(lst), tuple(lst1), tuple(lst2)
new_tuple_list = [tpl, tpl1, tpl2]
print(new_tuple_list)
