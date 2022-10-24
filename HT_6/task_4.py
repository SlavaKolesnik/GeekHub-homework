# 4. Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду 
# Морзе та виводить декодоване значення (латинськими літерами).
#    Особливості:
#     - використовуються лише крапки, тире і пробіли (.- )
#     - один пробіл означає нову літеру
#     - три пробіли означають нове слово
#     - результат може бути case-insensitive (на ваш розсуд - великими чи маленькими літерами).
#     - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо використовуватися не будуть. Лише латинські літери.
#     - додайте можливість декодування сервісного сигналу SOS (...---...)
#     Приклад:
#     --. . . -.- .... ..-- -...   .. ...   .... . .-. .
#     # результат: GEEKHUB IS HERE


def decode_from_morse():
    code = input('Введіть код морзе:\n').split()
    for x, morze in MorseCode_enSimbols.items():
        abcMorse[morze] = x
    for part in code:

        print("".join(abcMorse[part]), end='')


MorseCode_enSimbols = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                       'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-',
                       'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                       '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', "SOS": "...---..."}

abcMorse = {}

decode_from_morse()
