import psycopg2
import csv
from tabulate import tabulate

# Подключение к базе данных
conn = psycopg2.connect(host="localhost", dbname="lab10", user="postgres", password="Almaty250505", port=5432)
cur = conn.cursor()

# Создание таблицы, если она не существует
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL, 
    phone VARCHAR(255) NOT NULL
)
""")

# Функция для вставки данных с консоли или из CSV
def insert_data():
    print('Type "csv" or "con" to choose option between uploading csv file or typing from console: ')
    method = input().lower()
    if method == "con":
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    elif method == "csv":
        filepath = input("Enter a file path with proper extension: ")
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            for row in reader:
                cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", tuple(row))
    conn.commit()

# Функция для обновления данных
def update_data():
    column = input('Type the name of the column that you want to change: ')
    value = input(f"Enter {column} that you want to change: ")
    new_value = input(f"Enter the new {column}: ")
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s", (new_value, value))
    conn.commit()

# Функция для удаления данных
def delete_data():
    choice = input("Delete by (1) Name or (2) Phone? ")
    if choice == "1":
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    elif choice == "2":
        phone = input("Enter phone number to delete: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    print("Data deleted.")

# Функция для поиска по паттерну
def search_by_pattern():
    pattern = input("Enter pattern (part of name, surname, or phone): ")
    cur.execute("SELECT * FROM phonebook WHERE name LIKE %s OR surname LIKE %s OR phone LIKE %s", 
                ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

# Функция для вставки нового пользователя или обновления существующего
def insert_or_update_user():
    name = input("Name: ")
    surname = input("Surname: ")
    phone = input("Phone: ")
    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    if cur.fetchone():
        cur.execute("UPDATE phonebook SET name = %s, surname = %s WHERE phone = %s", (name, surname, phone))
        print("User updated!")
    else:
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
        print("New user added!")
    conn.commit()

# Функция для вставки нескольких пользователей с проверкой корректности телефона
def insert_multiple_users():
    users = [
        ("John", "Doe", "1234567890"),
        ("Alice", "Smith", "0987654321"),
        ("Bob", "Johnson", "12345")  # Некорректный номер телефона
    ]
    for user in users:
        name, surname, phone = user
        if len(phone) != 10:  # Проверка на корректность телефона
            print(f"Skipping invalid phone number for {name} {surname}: {phone}")
            continue
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    conn.commit()

# Функция для пагинации
def query_with_pagination():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

# Функция для отображения всех данных в таблице
def display_data():
    cur.execute("SELECT * from phonebook;")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

# Главный цикл для взаимодействия с пользователем
while True:
    print("""
    List of the commands:
    1. Type "i" or "I" in order to INSERT data to the table.
    2. Type "u" or "U" in order to UPDATE data in the table.
    3. Type "q" or "Q" in order to make specific QUERY in the table.
    4. Type "d" or "D" in order to DELETE data from the table.
    5. Type "s" or "S" in order to see the values in the table.
    6. Type "f" or "F" in order to close the program.
    """)

    command = input().lower()

    if command == "i":
        insert_data()
    elif command == "u":
        update_data()
    elif command == "d":
        delete_data()
    elif command == "q":
        search_by_pattern()
    elif command == "s":
        display_data()
    elif command == "f":
        break

# Закрытие соединения
conn.commit()
cur.close()
conn.close()
