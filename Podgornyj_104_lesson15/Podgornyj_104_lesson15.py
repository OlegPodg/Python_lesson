"""
Задание 2.
Файл содержит числа и буквы. Каждый записан в отдельной строке.
Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию,
а потом слова по возрастанию их длины

"""


def list_with_int_and_str():  # Объявляем функцию
    with open("example_lesson15_2.txt", 'r', encoding="utf-8") as ex2:
        list_1 = ex2.read().split('\n')  # разбиваем строку на части (\n - перенос строк), и возвращаем в виде списка
        list_digit = []  # Создаем пустой словарь для чисел
        list_alpha = []  # Создаем пустой словарь для букв
        for i in list_1:  # Запускаем цикл по списке list_1
            if i.isdigit():  # Если элемент состоит из цифр, то
                list_digit.append(i)  # добавляем элемент в список list_digit
            else:  # Если элемент состоит из букв, то list_alpha
                list_alpha.append(i)  # добавляем элемент в список
    # возвращаем сортировку списков
    return sorted(list_digit, key=lambda x: int(x)) + sorted(list_alpha, key=len)


print(list_with_int_and_str())  # Вызываем функцию

"""
Задача №3.
Создать файл, записать в него построчно данные, которые вводит пользователь.
Окончанием вводе пусть служит пустая строка.

"""


def file_empty():  # Объявляем функцию
    with open("example_lesson15_3.txt", 'w', encoding="utf-8") as ex3:  # Открываем файл "example_lesson15_3.txt"
        print("Введите строчки, если захотите закончить введите в новой строке enter:")
        while True:  # Запускаем цикл
            str_ = input("Введите строку (enter для выхода):")  # Запрос от пользователя на ввод данных
            if str_ != '':  # Если строка, введенная пользователем, не пустая, то
                ex3.write(str_ + '\n')  # Записываем строку в файл "example_lesson15_3.txt" и перенос строки
            else:
                break  # Если строка пустая, то заканчиваем цикл и закрываем файл "example_lesson15_3.txt"


file_empty()  # Вызываем функцию

"""
Задание №4.
В текстовом файле посчитать количество строк, а также для каждой отдельной строки
определить количество в ней символов.

"""


def file_verse():  # Объявляем функцию
    with open("example_lesson15_4.txt", 'r', encoding="utf-8") as ex4:  # Открываем файл example_lesson15_4.txt
        list_verse = ex4.read().split('\n')  # Разбиваем строку на части (\n - перенос строк), и возвращаем списком
        print(f"В тексте {len(list_verse)} строк.")  # Выводим на экран длину все строк
        count = 0  # Создаем счетчик для подсчета строк
        for i in list_verse:  # Запускаем цикл
            count += 1  # Прибавляем в счетчик 1 для отображения номера строки
            # Выводим на экран номер строки и количество символов в ней
            print(f"В {count} строке количество символов: {len(i)}")


file_verse()  # Вызываем функцию

"""
Домашнее задание
1. Создать файл.
2. Пишем функции (или функцию) для записи чисел и букв для разных строк файла.
3. Считываем информацию из файла таким образом, чтобы числа шли по возрастанию, а строки по возрастанию их длины.
Пример: 1 2 3 4 5 ода фига прикол степень

"""


def data_input():
    with open("lesson15.txt", 'w', encoding="utf-8") as dz_15:
        while True:  # Запускаем цикл
            word_user = input("Введите число или слова (enter для выхода в новой строке): ")  # Запрос от пользователя
            if word_user != "":  # Если строка не пустая, то проверяем условие
                if word_user.isdigit() or word_user.isalpha():  # Если строка состоит только из чисел или только из букв
                    dz_15.write(word_user + '\n')  # Записываем введенные данные
                else:  # Если строка написана сразу и буквы и числа в смешанном виде, то выводим сообщение
                    print("Вы ввели данные в смешенном виде!")
            else:  # Если строка введенная пользователем пуста, то
                break  # Останавливаем цикл


def list_with_int_and_str():
    with open("lesson15.txt", 'r', encoding="utf-8") as dz_15:
        list_1 = dz_15.read().split('\n')  # разбиваем строку на части (\n - перенос строк), и возвращаем в виде списка
        del list_1[-1]  # удаляем последний перенос (пустой элемент после переноса строки последнего элемента)
        list_digit = []  # Создаем пустой словарь для чисел
        list_alpha = []  # Создаем пустой словарь для букв
        for i in list_1:  # Запускаем цикл по списке list_1
            if i.isdigit():  # Если элемент состоит из цифр, то
                list_digit.append(i)  # добавляем элемент в список list_digit
        else:  # Если элемент состоит из букв, то list_alpha
            list_alpha.append(i)  # добавляем элемент в список
    # возвращаем сортировку списков
    return sorted(list_digit, key=lambda x: int(x)) + sorted(list_alpha, key=len)


data_input()  # Вызываем функцию data_input
print(list_with_int_and_str())  # Вызываем функцию list_with_int_and_str и выводим на экран результат
