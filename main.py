from secrets import choice
import string
import sqlite3

def create_list():
    _list = string.ascii_letters + string.digits + string.punctuation
    return _list

def create_password(password_length=8, _list=create_list()):
    password = [choice(_list) for i in range(password_length)]
    return ''.join(password)

def create_database():
    database = sqlite3.connect('database.db')
    return database

def queries():
    database = create_database()
    operator = database.cursor()
    name, select = inputs()
    insert(database, operator, name)
    if select:
        selects(operator)
    database.close()

def insert(database, operator, name):
    operator.execute(f'INSERT INTO passwords (NAME, PASSWORD)VALUES("{name}", "{create_password()}")')
    database.commit()

def selects(operator):
    operator.execute('SELECT * FROM passwords')
    print(operator.fetchall())

def inputs():
    name = input('name: ')
    select = bool(input('consult '))
    return name, select

if __name__ == '__main__':
    queries()