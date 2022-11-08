"""

Домашнее задание.
Два метода в классе, одни принимает в себя либо строку, либо число.
Если передается строка (*несколько слов на русском языке через пробел, без спецсимволов), то смотрим:
 - если произведение гласных и согласных букв меньше или равно длине слов, выводить все гласные,
иначе согласные.
 - если число то, произведение суммы чётных цифр на длину числа.
Длина строки и числа искать во втором методе.

"""


class Data:
    count_vowels = 0  # статический атрибут класса (счетчик для подсчета гласных букв)
    count_consonants = 0  # статический атрибут класса (счетчик для подсчета согласных букв)
    list_vowels = []  # статический атрибут класса (список для гласных букв)
    list_consonants = []  # статический атрибут класса (список для согласных букв)

    def __init__(self, input_user):  # Определим метод __init__ с параметрами self и input_user
        self.input_user = input_user

    def result(self):  # Определим метод result с параметрам self
        if self.input_user.replace(' ', '').isalpha():  # Если введенные данные состоит из букв
            for i in self.input_user.lower():  # Запускаем цикл
                if i in "уеыаоэяёию":  # Если элемент есть в "уеыаоэяёию", то
                    self.count_vowels += 1  # Прибавляем 1 к счетчику подсчета кол-ва гласных count_vowels
                    self.list_vowels.append(i)  # И добавляем элемент в список list_vowels

                elif i in "йцкнгшщзхфвпрлджчсмтб":  # Если элемент есть в "йцкнгшщзхфвпрлджчсмтб", то
                    self.count_consonants += 1  # Прибавляем 1 к счетчику подсчета кол-ва согласных count_consonants
                    self.list_consonants.append(i)  # И добавляем элемент в список list_consonants

            # Если произведение счетчика подсчета кол-ва гласных и счетчика подсчета кол-ва согласных меньше или равно
            # длине всех букв, то
            if self.count_vowels * self.count_consonants <= len(self.input_user.replace(' ', '')):
                return self.list_vowels  # Возвращаем все гласные буквы
            else:  # Если нет, то
                return self.list_consonants  # # Возвращаем все согласные буквы

        elif self.input_user.isdigit():  # Если введенные данные состоит из цифр
            sum_even = sum([int(a) for a in list(self.input_user) if int(a) % 2 == 0])  # Сумма всех четных цифр
            # Возвращаем произведение суммы всех чётных цифр и длины числа
            return sum_even * len(self.input_user)
        else:  # Если введенные не только буквы или цифры, то выводим сообщение
            print("Вы ввели некорректные данные! Нужно ввести либо число, либо строку")


# Запрос от пользователя ввести данные
input_ = input("Введите либо строку состоящую только из слов "
               "(пробел - можно использовать, спецсимволы (!,.?%;& и др.) - нет), либо число: ")
str_int = Data(input_)  # Создается объект класса Data
str_int.result()  # Обращаемся к методу result