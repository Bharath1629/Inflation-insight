# user_operations.py
import mysql.connector

def authenticate_user(conn, username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    data = (username, password)

    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(query, data)
        user = cursor.fetchone()

    return user
