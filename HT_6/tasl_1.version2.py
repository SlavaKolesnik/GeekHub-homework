# 1. Створіть функцію, всередині якої будуть записано СПИСОК із п'яти користувачів
# (ім'я та пароль). Функція повинна приймати три аргументи: два - обов'язкових
# (<username> та <password>) і третій - необов'язковий параметр <silent>
# (значення за замовчуванням - <False>).
# Логіка наступна:
#     якщо введено правильну пару ім'я/пароль - вертається True;
#     якщо введено неправильну пару ім'я/пароль:
#         якщо silent == True - функція повертає False
#         якщо silent == False - породжується виключення LoginException (його також треба створити =))


class LoginException(Exception):
    pass


def authorization(users, password, silent=False):


    users_pass = [['SobakaKusaka', 'Gav@Gava_3000'], ['KotyaraCarapaka', 'MurnyamX#$%$@'],
             ['VovkGrizyaka', 'Ay_Maugli1990'], ['KonyakaUdaryaka', 'Igogo777%%%'],
             ['GuskaShipaka', 'SHUUUU12$$$$']]


    try:

        if [users, password] in users_pass:
            return True
        raise LoginException('Невірний логін чи пароль')
    except LoginException as err:
        if silent:
            return False
        return err


print(authorization('SobakaKusaka', 'Gav@Gava_3000'))
print(authorization('KonyakaUdaryaka', 'asdasd', True))
print(authorization('asdasd', 'asdasd'))
