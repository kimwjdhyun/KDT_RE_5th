import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'user',
        password = '1234',
        database = 'codingon'
    )

def create_connection():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'user',
        password = '1234',
        database = 'codingon'
    )

