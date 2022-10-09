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
