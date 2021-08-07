from pymongo import MongoClient
import random

cluster = MongoClient("mongodb+srv://Freedom333:kires5889900@cluster0.0qqry.mongodb.net/Bankomat?retryWrites=true&w=majority")
db = cluster["Bankomat"]
collections = db["Bankomatcoll"]


class Bancomat():
    dictionary = {
        "ru": {
            "welcome": "\nДобро Пожаловать \"ALPHA BANK\" \n",
            "registration": "\nСоздать счет: 1\n"
                            "Войти в счет: 2\n",

            "menu": "\nВведите 1: чтобы пополнить счет\n" 
                    "Введите 2: чтобы снять Средство\n"
                    "Введите 3: чтобы отправить средство\n"
                    "Введите 4: чтобы просмотр баланса\n"   
                    "Введите 0: чтобы завершить операцию\n",

            "confirm": "\nНеправильное подверждение!!!\n",

            "warning": "\nНапоминаем что при отправке средств с вас "
                       "взимается плата в размере 1% от отправляемой суммы!\n"
                       "Чтобы подтвердить введите: 1\n"
                       "Чтобы отказать введите: 0\n",

            "again": "\nНапоминаем что пароль состоит только из 4-х цифр\n",

            "error_code": "\nВведен неправильный код карты\n",

            "error": "\nУ вас недостаточно средств!\n",

            "stop": "\nОперация Отменено\n",

            "card_code": "\nВведите код карты которого хотите отправить деньги:\n",

            "war": "\nВведен неправильная команда!\n",

            "confirm_card_code": "\nВведен неправильная карта пожалуйста проверьте и повторите\n",
        }
    }

    def __init__(self):
        self.try_count = 3

    def print_f(self, name_dict, name_massive):
        print(Bancomat.dictionary[name_dict][name_massive])

    # Наследует self.menu()
    # Пополняет баланс
    def add_money(self):
        add = float(input("Сколько хотите внести: "))
        balance = collections.find_one({"_id": self.idd})["balance"]
        collections.update_one({"_id": self.idd}, {"$set": {"balance": balance + add}})
        balance2 = collections.find_one({"_id": self.idd})["balance"]
        print(f"Ваш лицевой счет составляет {balance2} $")
        return self.menu()

    # наследует self.check_money_confirm()
    # выполняет снятие проверив подверждение у пользователя
    def check_money_update(self):
        self.print_f(name_dict='ru', name_massive="warning")
        user = str(input("Введите: "))
        if user == "1":
            collections.update_one({"_id": self.idd}, {"$set": {"balance": self.balance11 - self.add11}})
            balance2 = collections.find_one({"_id": self.idd})["balance"]
            print(f"Ваш лицевой счет составляет {balance2} $")
            return self.menu()
        elif user == "0":
            self.print_f(name_dict="ru", name_massive="stop")
            return self.menu()

    # наследует self.check_money()
    # проверяет хватит-ли средство для вывода
    def check_money_confirm(self):
        if self.add11 + (self.add11*0.01) <= self.balance11:
            return self.check_money_update()
        elif self.add11 + (self.add11*0.01) >= self.balance11:
            self.print_f(name_dict="ru", name_massive="error")
            return self.menu()

    # Наследует self.menu()
    # Снимет средство
    def check_money(self):
        self.add11 = float(input("Сколько хотите снять: "))
        self.balance11 = collections.find_one({"_id": self.idd})["balance"]
        return self.check_money_confirm()

    # Наследует self.send_money()
    # проверяет хватит-ли средств для отправки
    # отправляет денег
    def send_confirm(self):
        self.print_f(name_dict='ru', name_massive="warning")
        user = str(input("Введите: "))
        if user == "1":
            collections.update_one({"_id": self.idd}, {"$set": {"balance": self.balance1 - self.add}})
            balance = collections.find_one({"_id": self.card_code})["balance"]
            collections.update_one({"_id": self.card_code}, {"$set": {"balance": balance + add}})
        elif user == "0":
            self.print_f(name_dict="ru", name_massive="stop")
            return self.menu()

    # наследует self.send_money()
    # проверяет хватит-ли баланс на отправку
    def send_money_confirm(self):
        if self.add + (self.add*0.01) <= self.balance1:
            return self.send_confirm()
        elif self.add + (self.add*0.01) >= self.balance1:
            self.print_f(name_dict="ru", name_massive="error")
            return self.menu()

    # Наследует self.confirm()
    # отправляет денег
    def send_money(self):
        self.card_code = int(input("Введите карту: "))
        self.add = float(input("Сколько хотите отправить: "))
        self.balance1 = collections.find_one({"_id": self.idd})["balance"]
        return self.send_money_confirm()

    # Наследует self.confirm()
    # выводит баланс пользователя
    def view_balance(self):
        balance = collections.find_one({"_id": self.idd})["balance"]
        print(f"Ваш баланс составляет {balance} $")
        return self.menu()

    # меню функции
    # наследует self.menu()
    def confirm(self):
        if self.welcome == "1":
            return self.add_money()
        elif self.welcome == "2":
            return self.check_money()
        elif self.password == "3":
            return self.send_money()
        elif self.welcome == "4":
            return self.view_balance()
        elif self.welcome == "0":
            return self.reception()

    # Меню функции
    # наследует self.registration2()
    def menu(self):
        self.print_f(name_dict="ru", name_massive="welcome")
        self.print_f(name_dict="ru", name_massive="menu")
        self.welcome = str(input("Введите: "))
        return self.confirm()

    # запись нового пользователя в базу данных
    # наследует self.confirmed()
    def date_base(self):
        date = {
            "_id": self.id,
            "username": self.username,
            "card_code": self.password,
            "balance": self.balance
        }
        collections.insert_one(date)
        self.reception()

    # Одобряет регистрацию
    # наследует self.registration
    def confirmed(self):
        count = 3
        while count > 0:
            password2 = int(input("Подтвердите пароль: "))
            if self.password == password2:
                self.balance = float(input("Пополнить баланс: "))
                return self.date_base()
            else:
                count -= 1
                self.print_f(name_dict="ru", name_massive="confirm")
        return self.reception()

    # Наследует self.reception
    # Создает счет
    def registration(self):
        count = 3
        self.username = str(input("Имя пользователя: "))
        self.id = random.randrange(8600000000000000, 8600999999999999)
        print("Код вашей карты", self.id)
        while count > 0:
            self.password = int(input("Введите пароль карты: "))
            if self.password > 999 and self.password < 9999:
                self.confirmed()
                break
            else:
                count -= 1
                self.print_f(name_dict="ru", name_massive="again")

    # Наследует self.confirm_code_card()
    # вход в существующий счет
    def registration2(self):
        count = 3
        while count > 0:
            self.password = int(input("Введите пароль карты: "))
            password1 = collections.find_one({"_id": self.idd})["card_code"]
            if self.password == password1:
                return self.menu()
            else:
                count -= 1
                self.print_f(name_dict="ru", name_massive="error_code")
        return self.reception()

    # Наследует self.reception()
    # проверяет правильность карты
    def confirm_code_card(self):
        count = 3
        while count > 0:
            self.idd = int(input("Введите карту: "))
            if self.idd >= 8600000000000000 and self.idd <= 8600999999999999:
                self.registration2()
            else:
                self.print_f(name_dict="ru", name_massive="confirm_card_code")

    # Первая кодовая команда Наследует __init__(self)
    def reception(self):
        count = 3
        self.print_f(name_dict="ru", name_massive="registration")
        while count > 0:
            main_user = str(input("Введите: "))
            if main_user == "1":
                return self.registration()
            if main_user == "2":
                return self.confirm_code_card()
            else:
                count -= 1
                self.print_f(name_dict="ru", name_massive="war")


main = Bancomat()
main.reception()
