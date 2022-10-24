# 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
#    цифру;
#    - якесь власне додаткове правило :)
#    Якщо якийсь із параметрів не відповідає вимогам - породити виключення із відповідним текстом.

class LenPass(Exception):
    pass


class LenLog(Exception):
    pass


class Islower(Exception):
    pass


class Num(Exception):
    pass


def logpass(login, password):
    try:
        if len(login) < 3 or len(login) > 50:
            raise LenLog("ім'я повинно бути не меншим за 3 символа і не більшим за 50")
    except LenLog as err:
        print(err)
    try:
        if len(password) < 8:
            raise LenPass('пароль повинен бути не меншим за 8 символів')
    except LenPass as err:
        print(err)
    try:
        if password.islower():
            raise Islower('Пароль має бути з великої літери')
    except Islower as err:
        print(err)
    try:
        for i in password:
            if i in '0123456789':
                break
        else:
            raise Num('пароль повинен мати хоча б одну  цифру')
    except Num as err:
        print(err)


login = input('Введіть логін:\n')
password = input('Введіть пароль:\n')
logpass(login, password)
