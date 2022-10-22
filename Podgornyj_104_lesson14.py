"""

Домашнее задание.

Ввод с клавиатуры. Если строка введённая с клавиатуры - это число, то поделить первое на второе.
Обработать ошибку деления на ноль.
Если второе число 0, то программа запрашивает ввод чисел заново.
Также если были введены буквы, то обработать исключение.

"""


def input_number():
    while True:
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        try:
            result = int(num1) / int(num2)
            print(result)
        except ZeroDivisionError:
            result = 0
            print(f"Произошло деление на {result}. Введите числа заново.")

        except ValueError:
            print("Преобразование прошло неудачно! Вы ввели буквы вместо чисел! До свидание!")
            break


input_number()
