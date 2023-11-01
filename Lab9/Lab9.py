from tkinter import *
from tkinter import messagebox as mb
from tkinter.messagebox import showwarning
import os
import json
import string

if not os.path.exists('users.json'):
    with open('users.json', 'w') as f:
        json.dump([], f)
        pass

class Window:
    def __init__(self, width, height, title="Авторизация", resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+600+350")
        self.Login = Entry(self.root)
        self.Password = Entry(self.root, show="*")
    def run(self):
        self.registration()
        self.root.mainloop()

    def registration(self):
        Label(self.root, text="логин:", justify=LEFT).grid(row=0, column=0, sticky=W)
        self.Login.grid(row=0, column=1, sticky=W + E, padx=10, pady=10)

        Label(self.root, text="пароль:", justify=LEFT).grid(row=1, column=0, sticky=W)
        self.Password.grid(row=1, column=1, sticky=W + E, padx=10, pady=10)

        Button(self.root, text="Зарегестрироваться", width=15, command=self.save_data).grid(row=3, column=1, padx=20, pady=10, sticky=E)
        Button(self.root, text="Войти", width=10, command=self.vhod).grid(row=3, column=2, padx=5, pady=10, sticky=E)
        Button(self.root, text="Выйти", width=10, command=self.exit).grid(row=3, column=0, pady=10, sticky=E)

    def exit(self):
        choice = mb.askyesno("Выход","Вы хотите прекратить работу программы?")
        if choice:
            self.root.destroy()


    def save_data(self):
        login = self.Login.get()
        password = self.Password.get()

        if not login or not password:
            showwarning("Регистрация", "Пожалуйста, заполните все поля")
            return
        if len(login) <= 2:
            showwarning("Регистрация", "Имя пользователя должно быть длиннее 2 символов")
            return

        if len(password) < 8 or not any(char in password for char in string.punctuation):
            showwarning("Регистрация",
                        "Пароль должен быть длиннее 7 символов и содержать хотя бы один специальный символ")
            return

        with open("users.json", "r") as read_file:
            try:
                users_data = list(json.load(read_file))
            except json.JSONDecodeError:
                users_data = None

        with open("users.json", "w") as f:  # Проверка на наличие пользователя в базе
            user_is_exists = False
            if users_data is not None:
                for user in users_data:
                    if user['login'] == login:
                        user_is_exists = True
                        showwarning('Ошибка', 'Такое имя пользователя уже используется.')
                        json.dump(users_data, f)

            else:
                users_data = []
            if not user_is_exists:
                users_data.append({'login': login, "password": password})
                print('пользователь', login, 'зарегестрирован')
                mb.showinfo('Запись создана', 'Вы успешно зарегестрированы!')
                json.dump(users_data, f)
                self.root.destroy()

    def vhod(self):
        login = self.Login.get()
        password = self.Password.get()
        with open("users.json", "r") as read_file:
            try:
                users_data = list(json.load(read_file))
            except json.JSONDecodeError:
                users_data = None

        with open("users.json", "w") as file:  # Проверка на наличие пользователя в базе
            user_is_exists = False
            if users_data is not None:
                for user in users_data:
                    if user['login'] == login and user['password'] == password:
                        user_is_exists = True
                        mb.showinfo('Вход прошел успешно', 'Вход совершен')
                        self.root.destroy()

            if not user_is_exists:
                if users_data is None:
                    users_data = []
                showwarning('Ошибка', 'Неверное имя пользователя или пароль')
            json.dump(users_data, file)

    def button_action(self):
        Label(self.root, text="New label").pack()

window = Window(330,150)
window.run()
