# 7. Напишіть функцію, яка приймає 2 списки. Результатом має бути новий список,
# в якому знаходяться елементи першого списку, яких немає в другому. Порядок елементів, що залишилися має відповідати порядку в першому (оригінальному) списку.
# Реалізуйте обчислення за допомогою генератора в один рядок.
#     Приклад:
#     array_diff([1, 2], [1]) --> [2]
#     array_diff([1, 2, 2, 2, 3, 4], [2]) --> [1, 3, 4]


def lst1_lst2(lst1, lst2):
    return [x for x in lst1 if x not in lst2]


l1 = [1, 2], [1]
l2 = [1, 2, 2, 2, 3, 4], [2]


print(lst1_lst2(l1, l2))
