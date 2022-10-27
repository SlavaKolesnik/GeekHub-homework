# 6. Напишіть функцію,яка приймає рядок з декількох слів і повертає довжину найкоротшого слова.
# Реалізуйте обчислення за допомогою генератора в один рядок.


text = "Devils don't come from the Hell beneath us they come from the sky."
print(len(min(text.split(), key=len)))

