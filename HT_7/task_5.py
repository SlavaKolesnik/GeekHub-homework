# 5. Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих
# регістро-незалежних букв та цифр, які зустрічаються в рядку більше ніж 1 раз.
# Рядок буде складатися лише з цифр та букв (великих і малих). Реалізуйте обчислення
# за допомогою генератора в один рядок
#     Example (input string -> result):
#     "abcde" -> 0            # немає символів, що повторюються
#     "aabbcde" -> 2          # 'a' та 'b'
#     "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
#     "indivisibility" -> 1   # 'i' присутнє 6 разів
#     "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
#     "aA11" -> 2             # 'a' і '1'
#     "ABBA" -> 2             # 'A' і 'B' кожна двічі


def amount_str(lst):
    amount = set([x for x in lst.lower() if lst.lower().count(x) > 1])
    return len(amount)


print(amount_str('abcde'))
print(amount_str('aabbcde'))
print(amount_str('aabBcde'))
print(amount_str('indivisibility'))
print(amount_str('Indivisibilities'))
print(amount_str('aA11'))
print(amount_str('ABBA'))
