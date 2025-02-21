import sqlite3

### - Установка соединения с БД
##connection = sqlite3.connect('vkv_my_db.db')
##cursor = connection.cursor()
##
### - СОздание таблицы Users
##cursor.execute('''
##CREATE TABLE IF NOT EXISTS Users(
##id INTEGER PRIMARY KEY,
##username TEXT NOT NULL,
##email TEXT NOT NULL,
##age INTEGER
##)
##''')
##
##### - Создание индекса
####cursor.execute('CREATE INDEX idx_email ON Users(email)')
##
### - Добавление нового пользователя
##cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 30))
##
##### - Обновление записей
####cursor.execute('UPDATE Users SET age = ? WHERE username = ?',(29, 'newuser'))
##
##### - Удаление записей
###cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))
##
####cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
##
##### - Получаем средний возраст пользователей для каждого возраста 
####cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
####results = cursor.fetchall()
####for i in results:
####    print(i)
##    
##### - Фильтрация групп по среднему возросту больше 30
####cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
####filter_results = cursor.fetchall()
####for x in filter_results:
####    print(x)
##
##### - 1) Выбираем и сортируем пользователей по возрасту по убыванию 
####cursor.execute('SELECT username, age FROM Users ORDER BY age DESC')
####results = cursor.fetchall()
####for row in results:
####    print(row)
##
##### - 2) Выбираем и сортируем пользователей по возрасту по убыванию 
####cursor.execute('''
####SELECT username, age, AVG(age)
####FROM Users
####GROUP BY age
####HAVING AVG(age) > ?
####ORDER BY age DESC
####''', (27,))
####results = cursor.fetchall()
####for row in results:
####    print(row)
##
##### - Агрегатные функции 
####cursor.execute('SELECT COUNT(*) FROM Users')
####total_users = cursor.fetchone() [0]
####print('Общее количество пользователей:', total_users)
####cursor.execute('SELECT SUM(age) FROM Users') 
####total_age = cursor.fetchone() [0]
####print('Общее сумма возрастов пользователей:', total_age)
####cursor.execute('SELECT AVG(age) FROM Users') 
####average_age = cursor.fetchone() [0]
####print('Средний возраст пользователей:', average_age)
####cursor.execute('SELECT MIN(age) FROM Users') 
####min_age = cursor.fetchone() [0]
####print('Минимальный возраст пользователей:', min_age)
####cursor.execute('SELECT MAX(age) FROM Users') 
####max_age = cursor.fetchone() [0]
####print('Минимальный возраст пользователей:', max_age)
##
##### - Сложный запрос с объединением таблиц
####cursor.execute('''
####SELECT username, age
####FROM Users
####WHERE age = (SELECT MAX(age) FROM Users)
####''')
####oldest_users = cursor.fetchall()
####
####for user in oldest_users:
####    print(user)
##
##### - Вывод всех пользователей
####cursor.execute('SELECT * FROM Users')
####all_users = cursor.fetchall()
####for row in all_users:
####    print(row)
##
### ---------------------------------------------------
##### - Методы fetchone, fetchmany, fetchall
####cursor.execute('SELECT * FROM Users')
####first_user = cursor.fetchone() # первая запись
####print(first_user)
####first_five_user = cursor.fetchmany(5) # первые 5 записей
####print(first_five_user)
####all_users = cursor.fetchall() # все записи
####print(all_users)
##
##### - Преобразование данных в списки или словари
####cursor.execute('SELECT * FROM Users')
####users = cursor.fetchall()
####users_list = []
####for user in users:
####    user_dict = {
####        'id': user[0],
####        'username': user[1],
####        'email': user[2],
####        'age': user[3],
####    }
####users_list.append(user_dict)
####for u_l in users_list:
####    print(u_l)
##
##### - Обработка NULL - значений
####cursor.execute('SELECT * FROM Users WHERE age IS NULL')
####unknown_age_users = cursor.fetchall()
####for i in unknown_age_users:
####    print(i)
##
##### - Операторы BEGIN, COMMIT и ROLLBACK
####try:
####    # Начало транзакции
####    cursor.execute('BEGIN')
####    # Выполнение операции
####    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user1', 'user1@example.com'))
####    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user2', 'user2@example.com'))
####    # Подтверждение ихменений
####    cursor.execute('COMMIT')
####except:
####    # отмена транзакции в случае ошибки
####    cursor.execute('ROLLBACK')
####
##### - Автоматическое управление транзакциями
####import sqlite3
####with sqlite3.connection('vkv_my_db.db') as connection:
####    cursor = connection.cursor()
####    try:
####        # Начало транзакции автоматически
####        with connection:
####            cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user1', 'user1@example.com'))
####            cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user2', 'user2@example.com'))
####    except:
####        pass
##
##### - Продвинутые концепции
####query = 'SELECT * FROM Users WHERE age > ?'
####cursor.execute(query, (25,))
####users = cursor.fetchall()
####for user in users:
####    print(user)
####
##### - Представления (view)
##### - Создание представления для активных пользователей
####cursor.execute('CREATE VIEW ActiveUsers AS SELECT * FROM Users WHERE is_active = 1')
##### - Выбор активных пользователей
####cursor.execute('SELECT * FROM ActiveUsers')
####active_users = cursor.fetchall()
####for user in active_users:
####    print(user)
####
##### - Триггеры
####cursor.execute('''
####CREATE TABLE IF NOT EXISTS Users(
####id INTEGER PRIMARY KEY,
####username TEXT NOT NULL,
####email TEXT NOT NULL,
####age INTEGER,
####created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
####)
####''')
##### - Создание триггера
####cursor.execute('''
####CREATE TRIGGER IF NOT EXISTS update_created_at
####AFTER INSERT ON Users
####BEGIN
####UPDATE Users SET created_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
####END;
####''')
####
##### - Индексы
####cursor.execute('CREATE INDEX idx_username ON Users(username)')

# - Создание приложения
connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()
# - Создание таблы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tasks(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
status TEXT DEFAULT 'Not Started'
)
''')
# - Функция для добавления новой задачи
def add_task(title):
    cursor.execute('INSERT INTO Tasks (title) VALUES (?)', (title,))
    connection.commit()
# - Функция для обновления статуса задачи
def update_task_status(task_id, status):
    cursor.execute('Update Tasks SET status = ? WHERE id = ?', (status, task_id))
    connection.commit()
# - Функция для вывода списка задач
def list_tasks():
    cursor.execute('SELECT * FROM Tasks')
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)
# - Добавление задач
add_task('Подготовить презентацию')
add_task('Закончить отчет')
add_task('Одготовить ужин')
# - Обновление статуса задачи
update_task_status(2, 'In Progress')                   
# - Вывод списка задач
list_tasks()

connection.commit()
connection.close()
