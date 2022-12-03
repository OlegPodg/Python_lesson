import sqlite3
import csv

"""
Задание №5.
Создайте таблицу в Базе Данных с тремя колонками (id, 2 - text, 3 - text).
Заполните ее с помощью INSERT данными (3 записи).
Удалить с помощью DELETE 2-у запись. 
Обновить значения 3-ей записи: hellow world с помощью UPDATE.
Записать данные с таблицы в файл в три колонки.
Первая id, вторая и третья с данными
"""
with open("text.csv", "w+", encoding="cp1251", newline='') as tx:
    conn = sqlite3.connect("new_bd5.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS
            table_1(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                col_1 TEXT,
                col_2 TEXT)""")

    cursor.execute("""INSERT INTO table_1(col_1,col_2) VALUES("глянцевая","бумага")""")
    conn.commit()
    cursor.execute("""INSERT INTO table_1(col_1,col_2) VALUES("надувной","матрац")""")
    conn.commit()
    cursor.execute("""INSERT INTO table_1(col_1, col_2) VALUES("растворимый", "кофе")""")
    conn.commit()

    cursor.execute("""SELECT * FROM table_1""")
    print(cursor.fetchall())

    cursor.execute("""DELETE FROM table_1 WHERE id = 2""")
    conn.commit()

    cursor.execute("""SELECT * FROM table_1""")
    print(cursor.fetchall())

    cursor.execute("""UPDATE table_1 SET col_1 = "hellow", col_2 = "world" WHERE id = 3""")
    conn.commit()

    cursor.execute("""SELECT * FROM table_1""")
    data = cursor.fetchall()

    ex_writer = csv.writer(tx, delimiter=';')
    for row in data:
        ex_writer.writerow(row)

