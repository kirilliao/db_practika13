import sqlite3

# Создание подключения к БД (если файла нет, то он создастся)
connection = sqlite3.connect('vkv_my_db.db')

connection.close()
