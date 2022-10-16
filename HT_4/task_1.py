# 1. Написати функцiю season, яка приймає один аргумент
# (номер мiсяця вiд 1 до 12) та яка буде повертати пору року,
# до якої цей мiсяць належить (зима, весна, лiто або осiнь).
# У випадку некоректного введеного значення - виводити відповідне повідомлення.


try:
    def season(x):
        if x >= 3 and x <= 5:
            return 'весни'
        elif x >= 6 and x <= 8:
            return 'літа'
        elif x >= 9 and x <= 11:
            return 'осені'
        elif x >= 1 and x <= 12:
            return 'зими'
        else:
            print('В природі всього 12 місяців!')
            return season(int(input('Напиши від 1 до 12:\n')))


    result = season(int(input('Напишіть номер місяця:\n')))
    print('Це місяць', result)
except ValueError:
    print('Це не число!')
