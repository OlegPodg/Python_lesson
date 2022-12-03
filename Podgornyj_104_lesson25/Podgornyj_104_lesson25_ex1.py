import sqlite3

"""
Задание №1
Создайте новую Базу данных.
В ней создайте таблицу с тремя полями, два текстовых, одно - целое число.
Число запрашивается с клавиатуры, а слова задаются статически.
Выведите каждую запись в отдельную строку.

"""

conn = sqlite3.connect("new_bd1.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS
    table_1(
        number INTEGER, 
        col_1 TEXT, 
        col_2 TEXT
    )
""")

command_new = '''
    INSERT INTO table_1(number, col_1, col_2)
    VALUES(?,?,?)
'''
number_user = int(input("Введите число:"))
text_1 = "Hello"
text_2 = "Python"

cursor.execute(command_new, (number_user, text_1, text_2))
conn.commit()

for i in cursor.execute('''SELECT * FROM table_1'''):  # чтобы вывести каждую запись с новой строки используем цикл
    print(i)

