import pickle
import os
import time

# Декоратор для измерения времени выполнения метода
def timer_decorator(method):
    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time = time.time()
        print(f"Метод {method.__name__} выполнялся {end_time - start_time:.6f} секунд")
        return result
    return timed

# Декоратор для подсчета вызовов метода
def count_decorator(method):
    def counted(*args, **kw):
        counted.calls += 1
        result = method(*args, **kw)
        return result
    counted.calls = 0
    return counted

class Departments():
    ''' Класс отделов магазина '''
    def __init__(self, name, count_counters, count_sellers, number): 
        ''' Конструктор класса Departments'''
        self._name = name
        self._count_counters = count_counters
        self._count_sellers = count_sellers
        self._number = number
        self.staff = []  # Список сотрудников отдела
        self.goods = []  # Список товаров отдела

    @property
    @timer_decorator
    @count_decorator
    def name(self):
        ''' Возвращает название отдела '''
        return self._name

    @name.setter
    def name(self, new_name):
        ''' Устанавливает новое название отдела '''
        self._name = new_name

    @property
    def count_counters(self):
        ''' Возвращает количество касс в отделе '''
        return self._count_counters

    @count_counters.setter
    def count_counters(self, new_count_counters):
        ''' Устанавливает новое количество касс в отделе '''
        self._count_counters = new_count_counters

    @property
    def count_sellers(self):
        ''' Возвращает количество продавцов в отделе '''
        return self._count_sellers

    @count_sellers.setter
    def count_sellers(self, new_count_sellers):
        ''' Устанавливает новое количество продавцов в отделе '''
        self._count_sellers = new_count_sellers

    @property
    def number(self):
        ''' Возвращает номер отдела '''
        return self._number
    
    @property
    def staff(self):
        return self._staff
    
    @timer_decorator
    @count_decorator
    def add_staff_member(self, staff_member): # Добавление сотрудника в отдел
        self._staff.append(staff_member)
    
    @timer_decorator
    @count_decorator
    def add_goods(self, goods): # Добавление товара в отдел
        self._goods.append(goods)

    def __del__(self):
        ''' Деструктор класса Departments '''
        print(f'Department {self._name} with number {self._number} has been deleted.')

class MeatDepartments(Departments):
    ''' Класс мясных отделов '''
    def __init__(self, name, count_counters, count_sellers, number, temperature_range):
        ''' Конструктор класса MeatDepartments '''
        super().__init__(name, count_counters, count_sellers, number)
        self._temperature_range = temperature_range
    
    @property
    def temperature_range(self):
        ''' Возвращает температурный режим отдела '''
        return self._temperature_range
    
    @temperature_range.setter
    def temperature_range(self, new_temperature_range):
        ''' Устанавливает новый температурный режим отдела '''
        self._temperature_range = new_temperature_range
    
    def __del__(self):
        ''' Деструктор класса MeatDepartments '''
        print(f'Meat department {self._name} with number {self._number} has been deleted.')

class Staff():
    ''' Класс сотрудников магазина '''
    def __init__(self, surname, name, patronymic, department, year_of_birth, year_work, exp, post, gender, address, city, phone):
        ''' Конструктор класса Staff '''
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.department = department
        self.year_of_birth = year_of_birth
        self.year_work = year_work
        self.exp = exp
        self.post = post
        self.gender = gender
        self.address = address
        self.city = city
        self.phone = phone
        self.department.add_staff_member(self)
        department.staff.append(self)

    def FIO(self):
        ''' Возвращает ФИО сотрудника '''
        return (self.surname, self.name, self.patronymic)

    def __del__(self):
        ''' Деструктор класса Staff '''
        print(f'Staff member {self.surname} {self.name} {self.patronymic} has been deleted.')

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

class Seller(Staff):
    ''' Класс продавцов магазина '''
    def __init__(self, surname, name, patronymic, departments, year_of_birth, year_work, exp, post, gender, address, city, phone, sales_count):
        ''' Конструктор класса Seller '''
        super().__init__(surname, name, patronymic, departments, year_of_birth, year_work, exp, post, gender, address, city, phone)
        self._sales_count = sales_count
    
    @property
    def sales_count(self):
        ''' Возвращает количество продаж продавца '''
        return self._sales_count

    @sales_count.setter
    def sales_count(self, new_sales_count):
        ''' Устанавливает новое количество продаж продавца '''
        self._sales_count = new_sales_count

    def increment_sales_count(self):
        ''' Увеличивает количество продаж продавца на 1 '''
        self._sales_count += 1
    
    def __del__(self):
        ''' Деструктор класса Seller '''
        print(f'Seller {self.surname} {self.name} {self.patronymic} has been deleted.')
    
class Goods():
    ''' Класс товаров магазина '''
    def __init__(self, name, price, count, department):
        self._name = name
        self._price = price
        self._count = count
        self._department = department
        self._department.add_good(self)
        department.goods.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, new_count):
        self._count = new_count

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, new_department):
        self._department = new_department

    def __del__(self):
        print(f'Goods {self._name} has been deleted.')

    def __add__(self, other):
        ''' Перегрузка оператора сложения'''
        if isinstance(other, Goods):
            if self._name == other.name and self._department == other.department:
                return Goods(self._name, self._price + other.price, self._count + other.count, self._department)
            else:
                raise ValueError("Cannot add goods with different names or departments.")
        else:
            raise TypeError("Cannot add goods with non-Goods object.")

    def __sub__(self, other):
        ''' Перегрузка оператора вычитания'''
        if isinstance(other, Goods):
            if self._name == other.name and self._department == other.department:
                return Goods(self._name, self._price - other.price, self._count - other.count, self._department)
            else:
                raise ValueError("Cannot subtract goods with different names or departments.")
        else:
            raise TypeError("Cannot subtract goods with non-Goods object.")

    def __mul__(self, other):
        ''' Перегрузка оператора умножения'''
        if isinstance(other, (int, float)):
            return Goods(self._name, self._price * other, self._count * other, self._department)
        else:
            raise TypeError("Cannot multiply goods with non-numeric object.")

    def __truediv__(self, other):
        ''' Перегрузка оператора деления'''
        if isinstance(other, (int, float)):
            return Goods(self._name, self._price / other, self._count / other, self._department)
        else:
            raise TypeError("Cannot divide goods with non-numeric object.")


class SaleOfGoods():
    ''' Класс продажи товаров '''
    def __init__(self, goods, seller, count):
        ''' Конструктор класса SaleOfGoods '''
        self._goods = goods
        self._seller = seller
        self._count = count

    @property
    def goods(self):
        ''' Возвращает товар, проданный в данной продаже'''
        return self._goods

    @goods.setter
    def goods(self, new_goods):
        ''' Устанавливает новый товар, проданный в данной продаже '''
        self._goods = new_goods

    @property
    def seller(self):
        ''' Возвращает продавца, продавшего товар в данной продаже '''
        return self._seller

    @seller.setter
    def seller(self, new_seller):
        ''' Устанавливает нового продавца, продавшего товар в данной продаже '''
        self._seller = new_seller

    @property
    def count(self):
        ''' Возвращает количество товара, проданного в данной продаже '''
        return self._count

    @count.setter
    def count(self, new_count):
        ''' Устанавливает новое количество товара, проданного в данной продаже '''
        self._count = new_count
    
    def __str__(self):
        return "Sale of {0} by {1}, count: {2}".format(self.goods, self.seller, self.count)

    def __del__(self):
        ''' Деструктор класса SaleOfGoods '''
        print(f'Sale of goods {self._goods} has been deleted.')

class DepartmentError(Exception):
    ''' Класс исключений для класса Department'''
    def __init__(self, message):
        ''' Конструктор класса исключений для класса Department'''
        self.message = message
    
    def __str__(self):
        ''' Возвращает сообщение об ошибке '''
        return self.message
    
class StaffError(Exception):
    ''' Класс исключений для класса Staff'''
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

class GoodsError(Exception):
    ''' Класс исключений для класса Goods'''
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

class SaleOfGoodsError(Exception):
    ''' Класс исключений для класса SaleOfGoods'''
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

class SuperMarketDatabase():
    ''' Класс базы данных супермаркета '''
    def __init__(self):
        ''' Конструктор класса SuperMarketDatabase '''
        self._sales = []       # список продаж
        self._sellers = []     # список продавцов
        self._staff = []       # список сотрудников
        self._departments = [] # список отделов
    
    def save_database(self, db_file):
        ''' Сохраняет базу данных в файл '''
        with open(db_file, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_database(db_file):
        ''' Загружает базу данных из файла '''
        if os.path.exists(db_file):
            with open(db_file, 'rb') as f:
                return pickle.load(f)
        else:
            print('Database file does not exist')

    @staticmethod
    def delete_database(db_file):
        ''' Удаляет файл базы данных '''
        if os.path.exists(db_file):
            os.remove(db_file)
            print('Database file deleted')
        else:
            print('Database file does not exist')

    def add_sale(self, sale):
        ''' Добавляет продажу в базу данных '''
        self._sales.append(sale)
    
    def get_sales(self):
        return self._sales

    def add_seller(self, seller):
        ''' Добавляет продавца в базу данных '''
        self._sellers.append(seller)

    def add_staff(self, staff):
        ''' Добавляет сотрудника в базу данных '''
        self._staff.append(staff)

    def add_department(self, department):
        ''' Добавляет отдел в базу данных '''
        self._departments.append(department)

    def remove_sale(self, sale):
        ''' Удаляет продажу из базы данных '''
        self._sales.remove(sale)

    def remove_seller(self, seller):
        ''' Удаляет продавца из базы данных '''
        self._sellers.remove(seller)

    def remove_staff(self, staff):
        ''' Удаляет сотрудника из базы данных '''
        self._staff.remove(staff)

    def remove_department(self, department):
        ''' Удаляет отдел из базы данных '''
        self._departments.remove(department)

    def get_sales_by_seller(self, seller):
        ''' Возвращает список продаж по конкретному продавцу '''
        return [sale for sale in self._sales if sale.seller == seller]

    def get_sales_by_department(self, department):
        ''' Возвращает список продаж по конкретному отделу '''
        return [sale for sale in self._sales if sale.goods.department == department]

    def get_total_sales(self):
        ''' Возвращает общую сумму продаж '''
        return sum([sale.goods.price * sale.count for sale in self._sales])

    def get_total_sales_by_department(self, department):
        ''' Возвращает общую сумму продаж по конкретному отделу '''
        return sum([sale.goods.price * sale.count for sale in self.get_sales_by_department(department)])