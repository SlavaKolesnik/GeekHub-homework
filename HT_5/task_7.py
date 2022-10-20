# 7. Написати функцію, яка приймає на вхід список (через кому),
# підраховує кількість однакових елементів у ньому і виводить результат.
# Елементами списку можуть бути дані будь-яких типів.
#     Наприклад:
#     1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"


def dublikate(lst):
    lst_1 = list(zip(lst, map(type, lst)))
    lst_2 = []
    lst_3 = []
    for x in lst_1:
        if x in lst_2:
            pass
        else:
            lst_2.append(x)
            lst_3.append(f'{x[0]} повторюється раз: {lst_1.count(x)} ')
    print('\n'.join(lst_3))


lst = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]
dublikate(lst)
