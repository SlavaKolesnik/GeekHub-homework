# 2. Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати
# якийсь результат (напр. інпут від юзера, результат математичної операції тощо).
# Також створiть четверту ф-цiю, яка всередині викликає 3 попередні,
# обробляє їх результат та також повертає результат своєї роботи.
# Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.


def car(model):
    if model == 'Mustang':
        return model
    else:
        print("Це не твоя машина")


def speed(km):
    if km >= 100:
        mile = 100
        km = mile / 0.609
        return km
    else:
        exit('Зараз заглохнемо')


def gasoline(gas):
    return gas


def characteristics(model, km, gas):
    if gasoline(gas) >= 10:
        res = f'{car(model)} їде з швидкістю {speed(km)} км/год'
        return res
    else:
        exit('Мало бензину')


print(characteristics('Mustang',100, 50))
