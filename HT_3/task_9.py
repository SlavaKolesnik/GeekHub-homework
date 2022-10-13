# 9. Користувачем вводиться початковий і кінцевий рік. Створити цикл,
# який виведе всі високосні роки в цьому проміжку (границі включно).
# P.S. Рік є високосним, якщо він кратний 4, але не кратний 100,
# а також якщо він кратний 400.


try:
    number = int(input('enter the year from:\n'))
    n = int(input('enter the year to:\n'))
    for number in range(n + 1):
        if number % 4 == 0 and number != 100 and number != 400:
            print(number)
        else:
            pass


except (TypeError, ValueError):
    print("It's not a number")
