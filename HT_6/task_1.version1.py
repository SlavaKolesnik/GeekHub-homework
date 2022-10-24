# 1. Створіть функцію, всередині якої будуть записано СПИСОК із п'яти користувачів
# (ім'я та пароль). Функція повинна приймати три аргументи: два - обов'язкових
# (<username> та <password>) і третій - необов'язковий параметр <silent>
# (значення за замовчуванням - <False>).
# Логіка наступна:
#     якщо введено правильну пару ім'я/пароль - вертається True;
#     якщо введено неправильну пару ім'я/пароль:
#         якщо silent == True - функція повертає False
#         якщо silent == False - породжується виключення LoginException (його також треба створити =))


from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x500")
root.title('Вхід в систему')


def login():
    text = Label(text='Для входу в систему виберіть логін!')
    text_log = Label(text='Введіть цей логін:')
    enter_login = Entry()
    text_password1 = Label(text='Введіть ваш пароль:')
    enter_password1 = Entry(show="*")
    button_entry = Button(text='Ввійти!', command=lambda: log_pass())
    txt = 'SobakaKusaka, KotyaraCarapaka, VovkGrizyaka, KonyakaUdaryaka, GuskaShipaka'
    txt1 = 'Підказки логіну!'
    button_info_log = Button(text='Підказка логіну',
                         command=lambda: messagebox.showinfo(title=f'{txt1}', message=f'{txt}'))
    pss1 = 'Підказка пароля!'
    pss = 'Gav@Gava_3000, MurnyamX#$%$@ , Ay_Maugli1990, Igogo777%%%, SHUUUU12$$$$'
    button_ingfo_pass = Button(text='Підказка пароля',
                               command=lambda: messagebox.showinfo(title=f'{pss1}', message=f'{pss}'))
    text.pack()
    text_log.pack()
    enter_login.pack()
    text_password1.pack()
    enter_password1.pack()
    button_entry.pack()
    button_info_log.pack()
    button_ingfo_pass.pack()

    def log_pass():
        a = [['SobakaKusaka', 'Gav@Gava_3000'], ['KotyaraCarapaka', 'MurnyamX#$%$@'],
             ['VovkGrizyaka', 'Ay_Maugli1990'], ['KonyakaUdaryaka', 'Igogo777%%%'],
             ['GuskaShipaka', 'SHUUUU12$$$$']]
        for user in a:
            if enter_login.get() == user[0] and enter_password1.get() == user[1]:
                messagebox.showinfo(title='True', message='Ви успішно ввійшли')
                exit()
            else:
                messagebox.showerror(title='False', message='Ой-йой! Не вірний пароль!')
                return login()
        else:
            messagebox.showerror('Помилка такого логіну не існує!')
            return login()

login()
root.mainloop()

# Ця версія вам не сподобається бо вона не виконує усі вимоги завдання, тому там ще одна є)
