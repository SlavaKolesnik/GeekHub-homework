# 5. Написати функцію <fibonacci>, яка приймає один аргумент і
# виводить всі числа Фібоначчі, що не перевищують його.


def fibonacci():
    fib1 = 0
    fib2 = 1
    n = int(input('Введіть число:\n'))
    print(fib1, fib2, end=' ')
    for i in range(0, n):
        fib1, fib2 = fib2, fib1 + fib2
        if fib2 <= n:
            print(fib2, end=' ')


try:
    fibonacci()
except ValueError:
    print('Це не число!')


