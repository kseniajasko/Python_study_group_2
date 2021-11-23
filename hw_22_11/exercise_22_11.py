# 1. Створити функціонал, який ітеруватиме числа від 1 до 20:
#     - за допомогою класа-ітератора;
#     - за допомогою вираза-генератора (generator expression);
#     - за допомогою функції-генератора (generator function).
# 1.1
# class SimpleIterator:
#     def __iter__(self):
#         return self
#
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration
#
# s_iter1 = SimpleIterator(20)
# empty_list =[]
# for i in s_iter1:
#     empty_list.append(i)
# print(empty_list)

# 1.2
# list_numbers = [x for x in range(1, 21)]

# print(list_numbers)

#1.3

# def func_iter(number):
#     empty_list = []
#     i = 1
#     while i <= number:
#         empty_list.append(i)
#         i += 1
#     return empty_list

# print(func_iter(20))

# 2. Cтворити дві функції, які перевірятимуть, що заданий рядок є паліндромом (читається однаково в обох напрямках, без урахування пробілів). Перша функція має використати ітеративний підхід (через цикл), друга - рекурсивний.

# 2.1
# def is_palindrome(string):
#     string = string.lower()
#     word = ""
#     for i in string:
#         word = i + word
#     if string == word:
#         return True
#     else:
#         return False


# 2.2
# def is_palindrome_recursion(string):
#     string = string.lower()
#     l = len(string)
#     if l < 2:
#         return True
#     elif string[0] == string[l - 1]:
#         return is_palindrome_recursion(string[1: l - 1])
#     else:
#         return False
#
# s1 = "MalaYaLam"
# s2 = "Malaalam"
# print(is_palindrome(s1))
# print(is_palindrome_recursion(s1))

# 3. Перерахуйте та наведіть приклади якумога більшої кількості варіантів копіювання списку.

# 3
# import copy
#
# temp_list = [1, 5, 8, 10]
#
# new_list_1 = temp_list.copy()
# new_list_2 = list(temp_list)
# new_list_3 = temp_list[:]
# new_list_4 = copy.deepcopy(temp_list)
# new_list_5 = copy.copy(temp_list)
#
# new_list_6 = []
# for item in temp_list:
#     new_list_6.append(item)
#
# new_list_7 = []
# new_list_7.extend(temp_list)
#
# new_list_8 = [i for i in temp_list]
#
# print(new_list_1)
# print(new_list_2)
# print(new_list_3)
# print(new_list_4)
# print(new_list_5)
# print(new_list_6)
# print(new_list_7)
# print(new_list_8)

# 4. Перерахуйте та наведіть приклади якумога більшої кількості варіантів створення словників.

# 4
# # empty dictionary
# my_dict = {}
#
# # dictionary with integer keys
# my_dict_1 = {1: 'apple', 2: 'ball'}
#
# # using dict()
# my_dict_2 = dict({1:'apple', 2:'ball'})
#
# # from sequence having each item as a pair
# my_dict_3 = dict([(1,'apple'), (2,'ball')])
# print(my_dict)
# print(my_dict_1)
# print(my_dict_2)
# print(my_dict_3)

# 5. Створіть функцію, яка повертає довжину рядка, отриманого як аргумент. До неї створіть декоратор, який явно перетворює аргумент на рядок перед передаванням його задекорованій функції. Задекоруйте функцію через виклик декоратора та через синтаксис '@'. Поясніть, що таке декоратор. Завдяки чому можливо використання декораторів?


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         func(signature)
#     return wrapper
#
# @my_decorator
# def my_func(string):
#     print(type(string))
#
# my_func = my_decorator(my_func)
# my_func(4)

# Поясніть, що таке декоратор. Завдяки чому можливо використання декораторів?
# A decorator function is basically a function that adds new functionality to a function that is passed as argument.
# Using a decorator function is like adding chocolate sprinkles to an ice cream.
# It lets us add new functionality to an existing function without modifying it.
# A decorator is a design pattern in Python that allows a user to add
# new functionality to an existing object without modifying its structure.
# We can define a function inside another function in Python
# Functions can also be passed as parameters to other functions. A function can also generate another function.
# Python allows a nested function to access the outer scope of the enclosing function.
# This is a critical concept in decorators -- this pattern is known as a Closure.



# 6. Створіть клас, на прикладі методов якого покажіть два варіанти декорування методів класу декоратором property.

# class Portal:
#
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     # Getter method
#     def name(self):
#         return self._name
#
#     # Setter method
#     @name.setter
#     def name(self, val):
#         self._name = val
#
#     # Deleter method
#     @name.deleter
#     def name(self):
#         del self._name
#
#     @property
#     def upper_name(self):
#         return self.name.upper()
#
# portal_1 = Portal('First_portal')
# portal_2 = Portal('Two_portal')
# print(portal_1.upper_name)

# 7. Наведіть приклади отримання підрядка з рядка за індексами та з використанням об'єкту слайса
# string = "my company has 1000$ on profit, but I lost 500$ gambling."
# final_1 = int(string[15:19]) - int(string[43:46])
#
# slice_1 = slice(15, 19)
# slice_2 = slice(43, 46)
# final_2 = int(string[slice_1]) - int(string[slice_2])
#
# print(final_1)
# print(final_2)

# 8. Наведіть два приклади варіантів коректної роботи з файлом, коли закриття файлу після читання буде гарантоване
# 8.1
# with open("README.md") as readme:
#     long_description = readme.read()
# 8.2
# f=open('C:\\Tmp\\Script1.py', 'r')
# f.close()

# 9. Наведіть приклади двух функцій пошуку елементу у списку. Яку складність має кожен з них? Які обмеження у кожного з них?
# list_1 = [1, 5, 8, 10, 4]
#
# def linear_search(tmp_list, element):
#     for i in range(len(tmp_list)):
#         if tmp_list[i] == element:
#             return element
#     else:
#         return f'Not found'
#
# print(linear_search(list_1, 10))
# O(n)

# def binary_search(tmp_list, val):
#     first = 0
#     last = len(tmp_list)-1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first+last)//2
#         if tmp_list[mid] == val:
#             index = mid
#         else:
#             if val<tmp_list[mid]:
#                 last = mid -1
#             else:
#                 first = mid +1
#     return tmp_list[index]
#
# print(binary_search(list_1, 4))

# O(log n)
# НЕДОЛІК
# Бінарний пошук задається на впорядкованій множині шляхом неодноразового розподілу
# цієї множини на дві частини таким чином, що шуканий елемент потрапляє в одну з цих частин.


# 10. Створіть клас, який ілюструє можливіть створення нових об'єктів двома методами: через звичний __init__ та додатковий метод класу. Покажіть варіанти використання кожного з них.

# class Person:
#     all_person = []
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.all_person.append(self)
#
#     @staticmethod
#     def create_person(name, age):
#         return Person(name, age)
#
# person1 = Person('Ok', 'Sat')
# person2 = Person.create_person('Ok', 'Sat')
# print(Person.all_person)