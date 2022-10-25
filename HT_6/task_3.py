# 3. На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
#    а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по  
#    правилам своєї функції) - як валідні, так і ні;
#    б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить 
#    ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK
#    P.S. Не забудьте використати блок try/except ;)


class LenPass(Exception):
    pass


class LenLog(Exception):
    pass


class Islower(Exception):
    pass


class Num(Exception):
    pass


log_pass = [['SobakaKusaka', 'a'], ['KotyaraCarapaka', 'MurnyamX#$%$@'],
            ['Vo', 'Ay_Maugli1990'], ['KonyakaUdaryaka', 'gogo777%%%'],
            ['GuskaShipaka', 'SHUUUU12$$$$']]


def logpass(login, password):
    if len(login) < 3 or len(login) > 50:
        raise LenLog("ім'я повинно бути не меншим за 3 символа і не більшим за 50")

    if len(password) < 8:
        raise LenPass('пароль повинен бути не меншим за 8 символів')

    if password.islower():
        raise Islower('Пароль має бути з великої літери')

    for i in password:
        if i in '0123456789':
            break
    else:
        raise Num('пароль повинен мати хоча б одну  цифру')


for user in log_pass:
    status = "OK"
    try:
        logpass(user[0], user[1])
    except (LenLog, LenPass, Islower, Num) as error:
        status = error

    finally:
        print(f'Name: {user[0]}')
        print(f'Password: {user[1]}')
        print(f'Status: {status}')
        print('-----')
