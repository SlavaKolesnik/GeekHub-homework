# 1. Write a script that will run through a list of tuples and replace
# the last value for each tuple. The list of tuples can be hardcoded.
# The "replacement" value is entered by user. The number of elements
# n the tuples must be different.


list_tuple = [(13, 21, 32), ('Sakura', 'Pego', 'Qwerty'), (2.52, 124.456, 1234.345), ()]
def Remove(list_tuples):
    list_tuples = [t for t in list_tuples if t]
    return list_tuples

res = [t[:-1] + (100,) for t in Remove(list_tuple)]


print(res)
