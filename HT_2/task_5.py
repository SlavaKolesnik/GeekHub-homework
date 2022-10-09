# 5. Write a script which accepts a decimal number from
# user and converts it to hexadecimal.

text = 'Введіть дестякове число:'
print(f'{text:.^30}')
decimal = eval(input())
number = int(decimal)
res = hex(number)
print('Ваше десткове число:',decimal, 'дорівнює шістнадцядтковому:', res)
