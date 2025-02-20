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

###Создание индекса
##cursor.execute('CREATE INDEX idx_email ON Users(email)')

# Добавление нового пользователя
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 30))

### Обновление записей
##cursor.execute('UPDATE Users SET age = ? WHERE username = ?',(29, 'newuser'))

### Удаление записей
##cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

##cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))

### Получаем средний возраст пользователей для каждого возраста 
##cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
##results = cursor.fetchall()
##for i in results:
##    print(i)
##    
### Фильтрация групп по среднему возросту больше 30
##cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
##filter_results = cursor.fetchall()
##for x in filter_results:
##    print(x)

# Выбираем и сортируем пользователей по возрасту по убыванию 
cursor.execute('SELECT username, age FROM Users ORDER BY age DESC')
results = cursor.fetchall()
for row in results:
    print(row)

##connection.commit()
connection.close()
