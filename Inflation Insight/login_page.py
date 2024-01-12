import mysql.connector
from mysql.connector import Error


def display_login():
    print("1. Admin user")
    print("2. Normal user")
    print("3. New user")

def new_user_registration(conn,username, password):
    try:
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)
            create_user_query = f"INSERT INTO users (username, password,role) VALUES ('{username}', '{password}','user')"
            cursor.execute(create_user_query)
            conn.commit()

            print(f"Hi '{username}', Thanks for registration!")
            print("Welcome to Inflation project")
            print("Please Enter your credentials below")


    except Error as e:
        print(f"Error: {e}")