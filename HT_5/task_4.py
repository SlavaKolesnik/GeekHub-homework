# 4. Написати функцію <prime_list>, яка прийматиме 2 аргументи
# - початок і кінець діапазона, і вертатиме список простих чисел
# всередині цього діапазона. Не забудьте про перевірку на валідність
# введених даних та у випадку невідповідності - виведіть повідомлення.


def prime_list(a, b):
    if a < b:
        lst = []
        for i in range(a, b):
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    lst.append(i)
        print(lst)
    else:
        print('Значення "a" не може бути більше "b", чи йому дорівнювати!')


prime_list(1, 1000)
