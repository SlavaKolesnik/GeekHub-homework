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
