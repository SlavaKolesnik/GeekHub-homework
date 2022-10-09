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
