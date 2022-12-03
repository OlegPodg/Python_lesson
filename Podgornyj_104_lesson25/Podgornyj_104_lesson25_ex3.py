import sqlite3
import random

"""
Задание №3.
Создайте новую Базу данных.
Поля: id, 2 целочисленных поля.
Целочисленные поля заполняются рандомно от 0 до 9.
Выберите случайную запись из БД.
Если каждое число данной записи чётное, то удалите эту запись, если нечётное, то обновите данные в ней на (2,2)
"""

conn = sqlite3.connect("new_bd3.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS 
        table_1(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number1 INTEGER,
            number2 INTEGER
        )
""")

num_1 = random.randint(3, 3)
num_2 = random.randint(3, 3)

cursor.execute("""INSERT INTO table_1(number1, number2) VALUES(?,?)""", (num_1, num_2))
conn.commit()

cursor.execute("""SELECT * FROM table_1""")
result = cursor.fetchall()
print(result)
random_choice = random.choice(result)
print(random_choice)
id_random_choice = random_choice[0]
print(id_random_choice)

count_even = 0
count_odd = 0
for i in random_choice:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

if count_even == 3:
    cursor.execute("""DELETE FROM table_1 WHERE id = ?""", (id_random_choice,))
elif count_odd == 3:
    cursor.execute("""UPDATE table_1 SET number1 = 2, number2 = 2 WHERE id = ?""", (id_random_choice,))
conn.commit()

cursor.execute("""SELECT * FROM table_1""")
print(cursor.fetchall())
