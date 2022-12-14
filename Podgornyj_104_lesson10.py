# Задание 5
"""

Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
чтобы элементы первого списка были ключами, а элементы второго -
соответственно значениями нашего словаря.

"""
list_1 = ["BMW", "Audi", "Mercedes", "Nissan", "Subaru"]
list_2 = ["X7", "Q8", "GLA", "Murano", "Forester"]

dict_new = dict(zip(list_1, list_2))
print(dict_new)

# Задание 6

"""

Создайте словарь из строки 'pythonist' следующим образом:
в качестве ключей возьмите буквы строки, а значениями пусть
будут числа соответствующие количеству вхождений данной буквы в строку.

"""
string_ = 'pythonist'
dict_ = {a: string_.count(a) for a in string_}
print(dict_)

# Домашнее задание
"""

У вас есть словарь, где ключ - название продукта.
Значение - список, который содержит цену и количество товара.
Выведите через "-" название - цену - количество. 
С клавиатуры вводите название товара и его количество.
n - выход их программы.
Посчитайте цену выбранных товаров и сколько товаров осталось в изначальном списке

"""

dict_products = {'масло': [4, 20],  # создан словарь с продуктами
                 'хлеб': [1, 15],
                 'вино': [5, 17],
                 'мука': [3, 8],
                 'сахар': [2, 10]}

for key, value in dict_products.items():  # цикл для вывода всех товаров, цены и количества
    print(f"Товар: {key} - Цена: {value[0]} - Кол-во: {value[-1]}")


def products():  # Объявляем функцию products
    while True:  # Запускаем цикл, который нужно будет прервать break
        product_name = input("Введите название продукта: ")
        if product_name in dict_products:
            # Если товар закончился, выполняем данный блок if и завершаем итерацию
            if dict_products[product_name][-1] == 0:
                print("Данный товар закончился!")
                exit_1 = input("Введите n для выхода: ")  # Если пользователь хочет выйти, то нужно ввести 'n'
                if exit_1 == 'n':
                    break

            elif dict_products[product_name][-1] > 0:  # Если товар есть в наличии, выполняем данный блок elif
                quantity_goods = int(input("Введите количество продукта: "))
                # Уменьшаем количество товара
                dict_products[product_name][-1] = dict_products[product_name][-1] - quantity_goods
                # Выводим на экран стоимость выбранного товара (цена * количество приобретенного товара)
                print(f"Стоимость: {dict_products[product_name][0] * quantity_goods}")
                # Выводим на экран количество оставшегося товара, после покупки
                print(f"Осталось данного товара: {dict_products[product_name][-1]}")
                for i, y in dict_products.items():
                    print(f"Товар:{i} - Цена:{y[0]} - Кол-во:{y[-1]}")
                exit_2 = input("Введите n для выхода: ")  # Если пользователь хочет выйти, то нужно ввести 'n'
                if exit_2 == 'n':
                    break

            else:
                print("Вы ввели не верное количество товара!")  # Выводим сообщение если введено неправильное количество
                exit_3 = input("Введите n для выхода: ")  # Если пользователь хочет выйти, то нужно ввести 'n'
                if exit_3 == 'n':
                    break
        else:
            print("Вы ввели товар которого нет!")  # Выводим сообщение если товара нет в наличии
            exit_4 = input("Введите n для выхода: ")  # Если пользователь хочет выйти, то нужно ввести 'n'
            if exit_4 == 'n':
                break

    print("Итого осталось:")  # запускается цикл для вывода всех вывода оставшихся товаров, цены и количества
    for i, y in dict_products.items():
        print(f"Товар:{i} - Цена:{y[0]} - Кол-во:{y[-1]}")
    return dict_products  # Возвращаем словарь dict_products


products()  # Вызываем функцию products
