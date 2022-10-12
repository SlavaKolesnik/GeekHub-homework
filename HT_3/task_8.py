# 8. Створити цикл від 0 до ... (вводиться користувачем).
# В циклі створити умову, яка буде виводити поточне значення,
# якщо остача від ділення на 17 дорівнює 0.

try:
    sum = int(input('Enter a number: \n'))
    n = int(input('how many cycles to do: \n'))
    for i in range(1, n+1):
        x = sum % 17
        if x == 0:
            print(sum)
        else:
            break
except (TypeError, ValueError):
    print("It's not a number")
