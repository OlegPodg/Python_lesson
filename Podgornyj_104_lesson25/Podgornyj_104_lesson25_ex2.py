import sqlite3
import random

"""
Задание №2.
Создайте новую Базу данных.
Поля: id, 2 целочисленных поля
Целочисленные поля заполняются рандомно от 0 до 9.
Посчитайте среднее арифметическое всех элементов без учета id.
Если среднее арифметическое больше количества записей в БД, то удалите четвертую запись БД.
"""

conn = sqlite3.connect("new_bd2.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS
    table_1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number1 INTEGER, 
        number2 INTEGER
    )
""")

num_1 = random.randint(0, 9)
num_2 = random.randint(0, 9)

cursor.execute('''INSERT INTO table_1(number1, number2) VALUES(?,?)''', (num_1, num_2))
conn.commit()

cursor.execute('''SELECT number1, number2 FROM table_1''')
list_result = cursor.fetchall()
print(list_result)
sum_result = 0
for tuple_ in list_result:
    for i in tuple_:
        sum_result += i
print(sum_result)
average_result = (sum_result / (2 * len(list_result)))
print(average_result)

if average_result > len(list_result):
    cursor.execute("""DELETE FROM table_1 WHERE id = 4""")

cursor.execute("""SELECT * FROM table_1""")
print(cursor.fetchall())
