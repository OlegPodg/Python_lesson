import sqlite3

"""
Задание №4.
Создайте метод класса для работы с БД 
В БД:
Если передан 1 аргумент: вставить в таблицу запись с числом 3
Если переданы 2 аргумента: проверить первый или второй аргумент является числом.
Если условие верно, то удалить первую запись с БД
Если переданы 2 аргумента, их значения неизвестны, а 3 является числом, то обновить на число 77 запись3
"""

conn = sqlite3.connect("new_bd4.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS
        table_1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        num1 INTEGER)""")


class Sql:
    def sql_new_bd4(self, user_input1=None, user_input2=None, user_input3=None):
        if user_input1 is not None and user_input2 is None:
            cursor.execute("""INSERT INTO table_1(num1) VALUES (3)""")
            conn.commit()
        elif user_input1 is not None and user_input2 is not None:
            if type(user_input2) == int:
                cursor.execute("""DELETE FROM table_1 WHERE id = 1""")
                conn.commit()
        elif user_input1 is not None and user_input2 is not None and type(user_input3) == int:
            cursor.execute("""UPDATE table_1 SET num1 = 77 WHERE id = 3""")
            conn.commit()


obj_class = Sql()
obj_class.sql_new_bd4(1, 2, 3)
obj_class.sql_new_bd4("2", "2", 3)

cursor.execute("""SELECT * FROM table_1""")
print(cursor.fetchall())
