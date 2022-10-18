# Задача 3.
def date(day, month, year):
    list_months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля",
                   "августа", "сентября", "октября", "ноября", "декабря"]
    day_next = 0
    month_next = month
    year_next = year

    if month == "апреля" or month == "июня" or month == "сентября" or month == "ноября":
        if day == 30:
            day_next = 1
            month_next = list_months[list_months.index(month) + 1]
        elif 1 <= day <= 29:
            day_next = day + 1
        elif 0 > day or day >= 31:
            return "Вы ввели некорректное число дней"

    elif month == "февраля":
        if year % 4 == 0 and (year % 100 != 0 or year < 1582) or year % 400 == 0:
            if day == 29:
                day_next = 1
                month_next = "марта"
            elif 1 <= day <= 28:
                day_next = day + 1
            elif 0 >= day or day > 29:
                return "Вы ввели некорректное число дней"

        else:
            if day == 28:
                day_next = 1
                month_next = "марта"
            elif 1 <= day <= 27:
                day_next = day + 1
            elif 0 > day or day > 28:
                return "Вы ввели некорректное число дней"

    elif month == "декабря":
        if day == 31:
            day_next = 1
            month_next = "января"
            year_next = year + 1
        elif 1 <= day <= 30:
            day_next = day + 1
        else:
            return "Вы ввели некорректное число дней"

    else:
        if day == 31:
            day_next = 1
            month_next = list_months[list_months.index(month) + 1]
        elif 1 <= day <= 30:
            day_next = day + 1
        elif 0 > day or day > 31:
            return "Вы ввели некорректное число дней"

    return day_next, month_next, year_next


year_user = int(input("Введите год: "))
month_user = input("Введите месяц (буквами): ")
day_user = int(input("Введите день: "))

print(f"Следующая дата: {date(day_user, month_user, year_user)}")


#  Задача 10
def phone_words(user_words):  # Объявляем функцию и передаём параметр user_words
    count = ""  # Создаем счетчик (пустая строка)
    for i in user_words.upper():  # Создаем цикл для нашей введенной строки и применяем к ней метод upper
        for key, value in dict_phone.items():  # Создаем цикл для нашего словаря (для пары: ключ и значение)
            if i in value:  # Если элемент строки есть в значении словаря, то
                # ключ словаря преобразуем в строку и умножаем на индекс значения элемента + 1
                count += str(key) * (value.index(i) + 1)
    return count  # Возвращаем результат подсчета


dict_phone = {1: ".,?!:",
              2: "ABC",
              3: "DEF",
              4: "GHI",
              5: "JKL",
              6: "MNO",
              7: "PQRS",
              8: "TUV",
              9: "WXYZ",
              0: " "}

words = input("Введите текст на английском языке: ")
print(phone_words(words))  # Вызываем функцию phone_words и передаем аргумент words


# Задача 11
def list_data(data):  # Объявляем функцию list_data и передаём параметр data
    if len(data) == 0:  # Если список пуст
        return data
    elif type(data[0]) == list:  # Если первый элемент является списком
        l1 = data[0]
        l2 = data[1:]
        return list_data(l1) + list_data(l2)
    elif type(data[0]) != list:  # Если первый элемент не является списком
        l1 = [data[0]]
        l2 = data[1:]
        return l1 + list_data(l2)


list_ = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
# list_ = []
print(list_data(list_))
