import sqlite3

# Установка соединения с БД
connection = sqlite3.connect('vkv_my_db.db')
cursor = connection.cursor()

### СОздание таблицы Users
##cursor.execute('''
##CREATE TABLE IF NOT EXISTS Users(
##id INTEGER PRIMARY KEY,
##username TEXT NOT NULL,
##email TEXT NOT NULL,
##age INTEGER
##)
##''')

###Создание индекса
##cursor.execute('CREATE INDEX idx_email ON Users(email)')

### Добавление нового пользователя
##cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))

# Обновление записей
cursor.execute('UPDATE Users SET age = ? WHERE username = ?',(29, 'newuser'))


connection.commit()
connection.close()
