# 7. Write a script which accepts a <number>(int) from user and generates
# dictionary in range <number> where key is <number> and value is <number>*<number>
#     e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}

try:
    number = int(input('Enter a number: \n'))
    d = dict()

    for x in range(1, number + 1):
        d[x] = x * x

    print(d)
except (TypeError, ValueError):
    print("It's not a number")
