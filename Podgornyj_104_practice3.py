# Задание 1

"""1 пункт. Напишите рекурсивную функцию получения факториала числа n"""


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(6))


"""2 пункт. Напишите функцию, которая будет возвращать последовательность фиббоначи 
в заданном  диапазоне от 0 до n"""


def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


number = int(input("Введите число членов последовательности: "))
print("Последовательность Фибоначчи: ")
for i in range(number):
    print(fibonacci(i), end=" ")
print()

"""3 пункт. Дано 2 словаря (dict_1 и dict_2). 
Создайте словарь dict_3 таким образом, чтобы он был отсортирован по длине ключей из словарей dict_1 и dict_2"""

dict_1 = {'верный': [11, 55.2, 'слон'], 'фиолетовый': 15, 'орда': 'восемь'}
dict_2 = {'ода': {52, 99, 2}, 'сороконожка': {110, 'слово', 15}}
dict_new = {}
dict_new.update(dict_1)
dict_new.update(dict_2)
dict_3 = {}
for i in sorted(dict_new.keys(), key=len):
    dict_3.update({i: dict_new[i]})
print(dict_3)

# Задание 2
"""Дана строка. Выведите:"""


string_ = "Что это было?... Я не ожидал увидеть подобного, но мне придётся принять решение"

string_without_prep = string_[:]
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '

for i in string_without_prep.lower():
    if i not in alphabet:
        string_without_prep = string_without_prep.replace(i, '')
print(string_without_prep)  # 1. Строку без знаков препинания
print(string_.lower())  # 2. Строку без букв верхнего  регистра
print(string_.upper())  # 3. Всю строку в верхнем регистре
print(string_.swapcase())  # 4. Строку, изменив регистр букв (с нижнего на верхний и наоборот)
for i in string_.lower():
    if i not in alphabet:
        string_ = string_.replace(i, ' ')
print(string_)  # 5. Строку, заменив все знаки препинания на пробел
