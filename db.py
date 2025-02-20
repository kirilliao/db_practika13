import sqlite3

# - Установка соединения с БД
connection = sqlite3.connect('vkv_my_db.db')
cursor = connection.cursor()

# - СОздание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

### - Создание индекса
##cursor.execute('CREATE INDEX idx_email ON Users(email)')

# - Добавление нового пользователя
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 30))

### - Обновление записей
##cursor.execute('UPDATE Users SET age = ? WHERE username = ?',(29, 'newuser'))

### - Удаление записей
#cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

##cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))

### - Получаем средний возраст пользователей для каждого возраста 
##cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
##results = cursor.fetchall()
##for i in results:
##    print(i)
    
### - Фильтрация групп по среднему возросту больше 30
##cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
##filter_results = cursor.fetchall()
##for x in filter_results:
##    print(x)

### - 1) Выбираем и сортируем пользователей по возрасту по убыванию 
##cursor.execute('SELECT username, age FROM Users ORDER BY age DESC')
##results = cursor.fetchall()
##for row in results:
##    print(row)

### - 2) Выбираем и сортируем пользователей по возрасту по убыванию 
##cursor.execute('''
##SELECT username, age, AVG(age)
##FROM Users
##GROUP BY age
##HAVING AVG(age) > ?
##ORDER BY age DESC
##''', (27,))
##results = cursor.fetchall()
##for row in results:
##    print(row)

### - Агрегатные функции 
##cursor.execute('SELECT COUNT(*) FROM Users')
##total_users = cursor.fetchone() [0]
##print('Общее количество пользователей:', total_users)
##cursor.execute('SELECT SUM(age) FROM Users') 
##total_age = cursor.fetchone() [0]
##print('Общее сумма возрастов пользователей:', total_age)
##cursor.execute('SELECT AVG(age) FROM Users') 
##average_age = cursor.fetchone() [0]
##print('Средний возраст пользователей:', average_age)
##cursor.execute('SELECT MIN(age) FROM Users') 
##min_age = cursor.fetchone() [0]
##print('Минимальный возраст пользователей:', min_age)
##cursor.execute('SELECT MAX(age) FROM Users') 
##max_age = cursor.fetchone() [0]
##print('Минимальный возраст пользователей:', max_age)

### Сложный запрос с объединением таблиц
##cursor.execute('''
##SELECT username, age
##FROM Users
##WHERE age = (SELECT MAX(age) FROM Users)
##''')
##oldest_users = cursor.fetchall()
##
##for user in oldest_users:
##    print(user)

### - Вывод всех пользователей
##cursor.execute('SELECT * FROM Users')
##all_users = cursor.fetchall()
##for row in all_users:
##    print(row)

# ---------------------------------------------------
### - Методы fetchone, fetchmany, fetchall
##cursor.execute('SELECT * FROM Users')
##first_user = cursor.fetchone() # первая запись
##print(first_user)
##first_five_user = cursor.fetchmany(5) # первые 5 записей
##print(first_five_user)
##all_users = cursor.fetchall() # все записи
##print(all_users)

### - Преобразование данных в списки или словари
##cursor.execute('SELECT * FROM Users')
##users = cursor.fetchall()
##users_list = []
##for user in users:
##    user_dict = {
##        'id': user[0],
##        'username': user[1],
##        'email': user[2],
##        'age': user[3],
##    }
##users_list.append(user_dict)
##for u_l in users_list:
##    print(u_l)

# - Обработка NULL - значений
cursor.execute('SELECT * FROM Users WHERE age IS NULL')
unknown_age_users = cursor.fetchall()
for i in unknown_age_users:
    print(i)




##connection.commit()
connection.close()
