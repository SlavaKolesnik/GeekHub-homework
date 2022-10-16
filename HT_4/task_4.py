# 4. Наприклад маємо рядок -->
# "f98neroi4nr0c3n30irn03ien3c0rfe kdno400we(nw,kowe%00koi!jn35pijnp4 6ij7k5j78p3kj546p4 "
# "65jnpoj35po6j345" -> просто потицяв по клавi =)
#    Створіть ф-цiю, яка буде отримувати довільні рядки на зразок
# цього та яка обробляє наступні випадки:
# -  якщо довжина рядка в діапазоні 30-50 (включно) -> прiнтує довжину
# рядка, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всіх чисел та окремо рядок
# без цифр та знаків лише з буквами (без пробілів)
# -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)


import re


def abrakadabra():
    res = str(input('напишіть текст:\n'))
    if 30 <= len(res) <= 50:
        dict = {'Літери': 0, 'Числа': 0}
        for i in res:
            if i.isalpha():
                dict['Літери'] += 1
            elif i.isdigit():
                dict['Числа'] += 1
        print(dict, 'довжина рядка:', len(res))
    elif len(res) <= 30:
        a = "".join([x for x in res if x.isalpha()])
        print(a)
        numbers = 0
        for elem in res:
            if elem.isdigit():
                numbers += int(elem)
        print("сума чисел строки:", numbers)
    else:
        red = ''.join(sorted(set(res), key=res.index))
        string = red
        sorted_chars = sorted(string)
        sorted_string = ''.join(sorted_chars)
        alphabet = re.sub("[^A-Za-z][^0-9]", "", sorted_string)
        print(alphabet)


abrakadabra()
