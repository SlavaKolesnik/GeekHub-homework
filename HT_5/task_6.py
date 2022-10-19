# 6. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
# Тобто функція приймає два аргументи: список і величину зсуву (якщо ця величина
# додатна - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо
#  елементи з початку списку в його кінець).
#    Наприклад:
#    fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#    fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]


def shift(lst, value):
    if value < 0:
        value = abs(value)
        for x in range(value):
            lst.append(lst.pop(0))
    else:
        for x in range(value):
            lst.insert(0, lst.pop())


try:
    r = int(input('Введіть довжину списку:\n'))
    list_1 = list(range(1, r + 1))
    print(list_1)
    step = int(input('Введіть на скільки хочете його зсунути: \n'))
    shift(list_1, step)
    print(list_1)
except ValueError:
    print('Пишіть цілі числа!')
