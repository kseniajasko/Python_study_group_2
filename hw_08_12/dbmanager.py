import os.path
import sqlite3
from  sqlite3 import Error

CREATE_USERS_TABLE = '''CREATE TABLE IF NOT EXISTS user(
                    id integer PRIMARY KEY,
                    first_name text,
                    last_name text NOT NULL
                    );'''

CREATE_USER = '''INSERT INTO user(first_name, last_name), VALUES(?,?)'''
GET_USERS = '''SELECT * FROM user'''

class DBConnection:

    def __init__(self, db_file=None):
        if not db_file:
            db_file = os.path.join(os.getcwd(), 'database.db')
        self._connection = sqlite3.connect(db_file)

    def __enter__(self):
        return self._connection

    def __exit__(self, *args, **kwargs):
        self._connection.close()
        return True

# def create_connection(db_file):
#     try:
#         connection = sqlite3.connect(db_file)
#         return connection
#     except Error as e:
#         print(str(e))



def create_table(connection, sql_string):
    cursor = connection.cursor()
    cursor.execute(sql_string)

def create_user(connection, sql_string, user_data):
    cursor = connection.cursor()
    cursor.execute(sql_string, user_data)
    connection.commit()

def get_users(connection, sql_string):
    cursor = connection.cursor()
    cursor.execute(sql_string)
    data = cursor.fetchall()
    return data


if __name__ == '__main__':
    tmp_database = os.path.join(os.getcwd(), 'mydatabase.db')
    tmp_connection = DBConnection(tmp_database)
    create_table(tmp_connection, CREATE_USERS_TABLE)
    create_user(tmp_connection, CREATE_USER, ('Ivan', 'Ivanov'))
    users = get_users(tmp_connection, GET_USERS)






