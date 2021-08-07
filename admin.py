from pymongo import MongoClient
import datetime


cluster = MongoClient('mongodb+srv://User:NMsaa2003@cluster0.og4jy.mongodb.net/testdata?retryWrites=true&w=majority')
db = cluster['Bancomat']
product = db['product']
technique = db["Technique"]
Outfit = db['outfit']
users = db['usersofshoping']
# Функциии Администратора # Administrator functions


class Admin():
    dictionary = {
        "dict": "\nUsers: 1\n"
                "Products: 2\n"
                "Exit: 0 \n",

        "pass": "Login or password is incorrect!\n",

        "users": "\nA list of Users: 1\n"
                 "To change the date: 2\n"
                 "Delete user: 3\n"
                 "Exit: 0\n",

        "products": "\nAdd Product: 1\n"
                    "Add Technique: 2\n"
                    "Add OutFit: 3\n"
                    "Exit: 0\n",
        "defined": "\nYour command is defined\n",

        "ok": "OK: 1\n"
              "BACK: 0\n",
    }

    def __init__(self):
        self.name_admin = "Freedom"
        self.password_init = 5889900

    # Функция для вывода на экран текстов
    # Function for displaying text
    def printf_f(self, name_dict):
        print(self.dictionary[name_dict])


    # функция выводит список пользвателей наследует self.users()
    def view_users(self):
        i = 0
        for x in users.find({}, {'_id': 0, 'name': 1, 'fristname': 1, 'login': 1, 'password': 1, 'balance': 1}):
            i += 1
            print(i, 'name : ' + x['name'], '\n', 'fristname : ', x['fristname'], '\n', 'login : ', x['login'], '\n',
                  'password : ', x['password'], '\n', 'balance : ', x['balance'], '\n', )
        return self.admin_func()

    def change_date(self):
        users.update_one({"name": self.user_name, "fristname": self.frist_name, "login": self.user_login},
                         {'$set': {'login': self.new_name, 'password': self.new_login}})
        return self.admin_func()

    # подтверждение изменения наследует self.change_users_date()
    def change_date_users(self):
        count = 3
        while count > 0:
            self.printf_f(name_dict="ok")
            retry = str(input("Enter: "))
            if retry == "1":
                return self.change_date()
            elif retry == "0":
                return self.users()
            else:
                count -= 1
        self.printf_f(name_dict="defined")
        return self.admin_func()

    # Функци наследует self.users()
    # И изменяет данные
    def change_users_date(self):
        self.user_name = str(input("Name of user: "))
        self.frist_name = str(input('First name: '))
        self.user_login = str(input("Login: "))
        return self.change_users()

    def change_users(self):
        self.new_name = str(input('New login: '))
        self.new_login = input('New password: ')
        return self.change_date_users()

    # Функци наследует self.users
    # И удаляет данные пользователя
    def users_delete(self):
        # Нужно изменить
        user_name = str(input("Name of user: "))
        user_login = str(input("Login: "))
        user_password = input("Password: ")
        self.printf_f(name_dict="ok")
        retry = int(input("Enter:"))
        if retry == 1:
            pass
        elif retry == 0:
            return self.users()
        else:
            self.printf_f(name_dict="defined")

    # Функция работает с пользователями, наследует self.admin_func
    # Дает условия админу
    def users(self):
        self.printf_f(name_dict="users")
        count = 3
        while count > 0:
            users = str(input("Enter: "))
            if users == "1":
                return self.view_users()
            if users == "2":
                return self.change_users_date()
            elif users == "3":
                return self.users_delete()
            elif users == "0":
                return self.admin_func()
            else:
                self.printf_f(name_dict="defined")
                count -= 1
            return self.admin_func()

    def add_product_add(self):
        count = 3
        while count > 0:
            self.printf_f(name_dict="ok")
            admin = int(input("Add product: "))
            if admin == 1:
                product.insert_one(self.add_only_product)
                self.products()
            elif admin == 0:
                self.products()
            else:
                self.printf_f(name_dict="defined")
                count -= 1
            return self.products()

    # Функция наследует self.products
    # Добавляет продукт
    def add_product(self):
        id_product = int(input("Enter id product: "))
        production = input("Product: ")
        quantity = int(input('quantity: '))
        price = float(input('price: '))
        self.add_only_product = {
            "_id": id_product,
            'products': production,
            'quantity': quantity,
            'price': price,
        }
        return self.add_product_add()

    # Функция добавляет технику наследует self.add_technique()
    def add_technique_add(self):
        count = 3
        while count > 0:
            self.printf_f(name_dict="ok")
            admin = str(input("Add Technique: "))
            if admin == "1":
                technique.insert_one(self.add_only_tech)
                return self.products()
            elif admin == "0":
                return self.products()
            else:
                self.printf_f(name_dict="defined")
                count -= 1
        return self.products()

    # Функция наследует self.products
    # Добавляет технику
    def add_technique(self):
        id_product = int(input("Enter id Technique: "))
        production = input("Technique: ")
        quantity = int(input('quantity: '))
        price = float(input('price: '))
        self.add_only_tech = {
            "_id": id_product,
            'products': production,
            'quantity': quantity,
            'price': price,
        }
        return self.add_technique_add()

    def add_outfit_add(self):
        count = 3
        while count > 0:
            self.printf_f(name_dict="ok")
            admin = str(input("Add OutFit: "))
            if admin == "1":
                Outfit.insert_one(self.add_only_outfit)
                return self.products()
            elif admin == "0":
                return self.products()
            else:
                self.printf_f(name_dict="defined")
                count -= 1
        return self.products()

    def add_outfit(self):
        id_product = int(input("Enter id OutFit: "))
        production = input("OutFit: ")
        quantity = int(input('quantity: '))
        price = float(input('price: '))
        self.add_only_outfit = {
            "_id": id_product,
            'products': production,
            'quantity': quantity,
            'price': price,
        }
        return self.add_outfit_add()

    # Функция работает с продуктами, наследует self.admin_func
    # Дает условия админу
    def products(self):
        count = 3
        while count > 0:
            self.printf_f(name_dict="products")
            products = str(input("Enter: "))
            if products == "1":
                return self.add_product()
            elif products == "2":
                return self.add_technique()
            elif products == "3":
                return self.add_outfit()
            elif products == "0":
                return self.admin_func()
            else:
                count -= 1
        return self.admin_func()

    # Функция имеет доступ к продуктам или пользователям, наследует self.admin
    def admin_func(self):
       count = 3
       while count > 0:
            self.printf_f(name_dict="dict")
            user_product = str(input("Enter: "))
            if user_product == "1":
                return self.users()
            elif user_product == "2":
                return self.products()
            elif user_product == "0":
                return
            else:
                count -= 1
       return

    # Вход в систему как администратор
    def admin(self):
        count = 3
        while count > 0:
            login = input("\nLogin: ")
            password = int(input("Password: "))
            if password == self.password_init and login == self.name_admin:
                print(f"{datetime.now()}\nВход в систему как администратор прошло успешно!")
                return self.admin_func()
            elif password != self.password_init or login != self.name_admin:
                count -= 1
                self.printf_f(name_dict="pass")


main = Admin()
main.admin()