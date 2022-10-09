# 7. Write a script to concatenate all elements in
# a list into a string and print it. List must include
# both strings and integers and must be hardcoded.

my_list = ([1, 2, 4, True, 'Alabai', 'exodus', '@#@!#$$', False, 2.34, 66.1, 'J0$T0'])
res = "".join([str(_) for _ in my_list])
print(res)
