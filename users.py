# from datetime import datetime
# import random
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://User:NMsaa2003@cluster0.og4jy.mongodb.net/testdata?retryWrites=true&w=majority')
db = cluster['Bancomat']
product = db['product']
electrinics = db["Technique"]
Outfit = db['outfit']
users = db['usersofshoping']


class UzAmazon():

    def __init__(self):
        self.i = 0
        self.the_answers = {
            'errors': {
                'log_or_reg_error': '- Вы ввели не существующие данные',
                'registration_error': '- Вы ввели не верные данные',
                'compiler': '- Вы истратили все попытки, вернитесь позже',
            },
            'user_response': {
                'log_or_reg': '1 - Регистрация\n2 - Вход',
                'registration': '1 - Имя\n2 - Фамилия\n3 - Логин\n4 - Пароль\n5 - Баланс',
                'log': '1 - Логин\n2 - Пароль',
                'menu_in_amazon': '1 - Покупка\n2 - Пополнение баланса\n0 - Выйти',
                'shopping': '1 - Продукты питания\n2 - Одежды\n3 - Техника\n0 - Выйти',
                'balance_nums' : '- Не достаточно средств или вы ввели больше чем количество(масса) продукта',
                'chek_log' : '- Вы ввели не верные данные',
                'removes_quantity' : '-Покупка прошло успешно'
            },
        }

        self.log_or_reg()

    # ФУНКЦИЯ ДЛЯ ПРИНТА
    def output(self, arg1, arg2):
        x = self.the_answers[arg1][arg2]
        print(x)

    # Анализ Какой тип товара хочет купить клиент
    def analysis(self):
        if self.name_func_shop == 4:
            self.arguments = product
            self.balance_nums(argument=self.food_num, argument1=product)
        elif self.name_func_shop == 8:
            self.arguments = electrinics
            self.balance_nums(argument=self.food_num, argument1=electrinics)
        elif self.name_func_shop == 12:
            self.arguments = Outfit
            self.balance_nums(argument=self.food_num, argument1=Outfit)

    # Проверка
    def balance_nums(self, argument, argument1):
        sum = argument1.find_one({'_id': argument})['quantity']
        the_cost = argument1.find_one({'_id': argument})['price']
        x = self.food_num_many * the_cost
        if sum < self.food_num_many or self.balance < x :
            self.output(arg1='user_response', arg2= 'balance_nums')
            self.i = 0
            self.shopping(func_name= 99)
        else:
            self.removes_quantity(arg=self.food_num, arg0=self.food_num_many, argument2=self.arguments)

    # ОТНИМАЕТ от количество товара
    def removes_quantity(self, arg, arg0,argument2):
        sum = argument2.find_one({'_id': arg})['quantity']
        the_cost = argument2.find_one({'_id': arg})['price']
        many = users.find_one({'login': self.log_entr, 'password': self.password_entr})['balance']
        sum2 = many - the_cost * arg0
        sum -= arg0
        users.update_one({'login': self.log_entr, 'password': self.password_entr},{"$set": {"balance": sum2}} )
        argument2.update_one({"_id": arg}, {"$set": {"quantity": sum}})
        # self.balance -= the_cost * arg0
        self.output(arg1='user_response', arg2='removes_quantity')
        self.shopping(func_name= 99)

    # Выведит количество родуктов
    def productsamazon(self):
        for x in product.find({}, {'_id': 1, 'products': 1, 'techno': 1, 'quantity': 1, 'price': 1}):
            print('{} - Your product: {}, Price: {}$'.format(x['_id'],x['products'],x['price'],x['price']))

    # ГЛАВНЫЙ КОМПИЛЯТОР
    def compiler(self):
        self.i += 1
        if self.i < 3:
            self.all_functions_copiler()
        elif self.i >= 3:
            self.output(arg1='errors', arg2='compiler')
            self.full_temp()

# ПЕРЕЗАПИШЕТ НОМЕРРА ФУНКЦИЙ
    def all_functions_copiler(self):
        if self.name_func == 1:
            # self.all_functions()
            self.registration()
        elif self.name_func == 2:
            self.log()
            # self.all_functions()
        elif self.name_func == 99:
            self.glav_menu(func_name= 99)
        elif self.name_func == 3:
            self.name_func = 100
            self.shopping(func_name=99)
        elif self.name_func == 6:
            self.balance_replenishment()
        elif self.name_func == 0:
            self.log_or_reg()
        elif self.name_func_shop == 4:
            self.food_products()
        elif self.name_func_shop == 8:
            self.clothes()
        elif self.name_func_shop == 12:
            self.technics()
        elif self.name_func_shop == 0:
            self.glav_menu(func_name= 99)

# ОТПРАВЛЯЕТ В ФУНКЦИИ КОГДА ИСТРАТИТ ВСЕ ПОПЫТКИ
    def full_temp(self):
        self.i = 0
        if self.name_func == 0 or self.name_func == 1 or self.name_func == 2 or self.name_func == 3 or self.name_func == 6 or self.name_func == 99:
            self.log_or_reg()
        elif self.name_func_shop == 4 or self.name_func_shop == 8 or self.name_func_shop == 12:
            self.glav_menu(func_name= 0)
        else:
            self.log_or_reg()

    # вход либо регистрация 11111
    def log_or_reg(self):
        try:
            self.output(arg1='user_response', arg2='log_or_reg')
            self.name_func = int(input(': '))
            self.name_func *= 1
            self.all_functions_copiler()
        except:
            self.output(arg1='errors', arg2='log_or_reg_error')
            self.log_or_reg()

    # РЕГИСТРАЦИЯ
    def registration(self):
        self.output(arg1='user_response', arg2='registration')
        try:
            self.name = str(input('-1: '))
            self.fristname = str(input('-2: '))
            self.log_entr = input('-3: ')
            self.password_entr = int(input('-4: '))
            self.balance = float(input('-5: '))
            self.name_func = 99
            self.i = 0
            self.registration_db()
            self.all_functions_copiler()
        except:
            self.output(arg1='errors', arg2='registration_error')
            self.compiler()

    # Добавление регистрацфии в Mongodb
    def registration_db(self):
        a = {
            'name':self.name ,
            'fristname': self.fristname,
            'login': self.log_entr,
            'password': self.password_entr,
            'balance' : self.balance,
        }
        users.insert_one(a)

    # Вход 2222
    def log(self):
        try:
            self.output(arg1='user_response', arg2='log')
            self.log_entr = input('-1: ')
            self.password_entr = int(input('-2: '))
            self.admin()
            # self.check_log()
        except:
            if self.i == 2:
                self.name_func = 0
            self.output(arg1='errors', arg2='log_or_reg_error')
            self.compiler()

    def admin(self):
        try:
            cheklog = users.find_one({'login': self.log_entr, 'password': self.password_entr})['login']
            chek = users.find_one({'login': self.log_entr, 'password': self.password_entr})['password']
            if cheklog == 'Freedom' and chek == 5889900:
                from .admin import main
            else:
                self.check_log()
        except:
            self.log_or_reg()

    # Вход в аккаунт
    def check_log(self):
        cheklog = users.find_one({'login': self.log_entr, 'password': self.password_entr})['login']
        chekpassword = users.find_one({'login': self.log_entr, 'password': self.password_entr})['password']
        if self.log_entr == cheklog and self.password_entr == chekpassword:
            self.i = 0
            self.data_equalization()
        else:
            self.output(arg1= 'user_response', arg2='chek_log')
            self.compiler()

    # приравнения при входе
    def data_equalization(self):
        many_data = users.find_one({'login': self.log_entr, 'password': self.password_entr})['balance']
        self.balance = many_data
        self.glav_menu(func_name=99)

# Главное мню 3333
    def glav_menu(self, func_name):
        self.output(arg1='user_response', arg2='menu_in_amazon')
        try:
            self.name_func = int(input(': '))
            self.name_func *= 3
            self.i = 0
            self.all_functions_copiler()
        except:
            self.output(arg1='errors', arg2='log_or_reg_error')
            self.name_func = func_name
            self.compiler()

    # ПОПОЛНЕНИЕ БАЛАНСА
    def balance_replenishment(self):
        many = users.find_one({'login': self.log_entr, 'password': self.password_entr})['balance']
        print('- Ваш баланс в текущее время: {}$\n- Введите сумму ввода: '.format(many))
        many_num = float(input(': '))
        many_num += many
        users.update_one({"login": self.log_entr}, {"$set": {"balance": many_num}})
        self.glav_menu(func_name=99)

# ПОКУКИ 4444
    def shopping(self, func_name):
        self.output(arg1='user_response', arg2='shopping')
        try:
            self.name_func_shop = int(input(': '))
            self.name_func_shop *= 4
            self.shopping_check()
        except:
            self.output(arg1='errors', arg2='log_or_reg_error')
            self.name_func = func_name
            self.compiler()

    # Проверка соответствует ли данные к сущестствующи данным
    def shopping_check(self):
        if self.name_func_shop == 0 or self.name_func_shop == 4 or self.name_func_shop == 8 or self.name_func_shop == 12:
            self.i = 0
            self.all_functions_copiler()
        else:
            self.output(arg1='errors', arg2='log_or_reg_error')
            self.name_func = 3
            self.compiler()

    # ПРОДУКТЫ ПИТАНИЯ
    def food_products(self):
        self.productsamazon()
        try:
            self.food_num = int(input(': '))
            self.food_num_many = int(input('- Введите массу(кг): '))
            self.analysis()
            # self.removes_quantity(arg=self.food_num, arg0=self.food_num_many)
        except:
            self.output(arg1='errors', arg2='log_or_reg_error')
            self.compiler()

    # ОДЕЖДЫ
    def clothes(self):
        "заходит в одел одежд и "
        self.productsamazon()
        try:
            self.food_num = int(input(': '))
            self.food_num_many = int(input('- Введите кол-во: '))
            self.analysis()
            # self.removes_quantity(arg=self.food_num, arg0=self.food_num_many)
        except:
            self.output(arg1='errors', arg2='log_or_reg_error')
            self.compiler()

    # ТЕХНИКИ
    def technics(self):
        self.productsamazon()
        try:
            self.food_num = int(input(': '))
            self.food_num_many = int(input('- Введите кол-во: '))
            self.analysis()
            # self.removes_quantity(arg=self.food_num, arg0=self.food_num_many)
        except:
            self.output(arg1='errors', arg2='log_or_reg_error')
            self.compiler()


a = UzAmazon()
