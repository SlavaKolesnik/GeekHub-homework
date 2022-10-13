# 8. Створити цикл від 0 до ... (вводиться користувачем).
# В циклі створити умову, яка буде виводити поточне значення,
# якщо остача від ділення на 17 дорівнює 0.

try:
    s = int(input('enter the number:\n'))
    for x in range(0, s):
        if x % 17 == 0:
            print(x)


except ValueError:
    print("enter a number")
