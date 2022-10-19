# 3. Написати функцию <is_prime>, яка прийматиме 1 аргумент
# - число від 0 до 1000, и яка вертатиме
# True, якщо це число просте і False - якщо ні.


def is_prime():
    x = float(input('Введіть від 0 до 1000:\n'))
    if x <= 1000:
        if x % 1 == 0:
            return True
        else:
            return False
    print('Число не в діапазоні від 0 до 1000!')
    return is_prime()


try:
    print(is_prime())
except ValueError:
    print('Це не число!')
