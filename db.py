import sqlite3

# Установка соединения с БД
connection = sqlite3.connect('vkv_my_db.db')
cursor = connection.cursor()

# СОздание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

# Сохранение изменения и закрывание соединения
connection.commit()
connection.close()
