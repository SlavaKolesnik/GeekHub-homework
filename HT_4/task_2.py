# 2. Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати
# якийсь результат (напр. інпут від юзера, результат математичної операції тощо).
# Також створiть четверту ф-цiю, яка всередині викликає 3 попередні,
# обробляє їх результат та також повертає результат своєї роботи.
# Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.


import random
from termcolor import cprint
import time


def you_age():
    var1 = int(input('Скільки тобі років: \n'))
    while var1 >= 1:
        if var1 >= 18:
            destiny(var1)
            return var1
        else:
            exit('Повертайся, коли підростеш!')


def you_laki():
    number = random.randint(1,6)
    cprint('Дістаємо револьвер. Крутимо барабан!', color='blue')
    time.sleep(2)
    return number


def taken_numre():
    gues = int(input('Спробуй вгадати від 1 до 6:\n'))
    if gues <= 6:
        time.sleep(2)
        return gues
    else:
        exit('Ти не вмієш рахувати!')


def destiny(var1):
    age = var1 + 1
    if you_laki() == taken_numre():
        cprint(f'{my_name}, cьогодні твій день! Зіграємо ще раз коли буде {age} років.', color='cyan')
    else:
        cprint(f'{my_name}, ти програв! Нажаль {age} років тобі вже не буде!', color='red')


try:
    my_name = input('Введіть імя:\n')
    you_age()
except ValueError:
    print('Це не число!')
