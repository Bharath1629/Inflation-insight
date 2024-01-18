# admin_operations.py
import mysql.connector
from mysql.connector import Error
def authenticate_user(conn, username, password,role):
    query = "SELECT * FROM users WHERE username = %s AND password = %s AND role=%s"
    data = (username, password,role)

    with  conn.cursor(dictionary=True) as cursor:
        cursor.execute(query, data)
        user = cursor.fetchone()

    return user if user else None
def create_user_by_admin(conn,username, password,role):
    try:
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)
            create_user_query = f"INSERT INTO users (username, password,role) VALUES ('{username}', '{password}','{role}')"
            cursor.execute(create_user_query)
            conn.commit()

            print(f"User '{username}' created successfully by admin.")


    except Error as e:
        print(f"Error: {e}")


def update_user_by_admin(conn,username, new_password):
    try:
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)
            update_user_query = f"UPDATE users SET password = '{new_password}' WHERE username = '{username}'"
            cursor.execute(update_user_query)
            conn.commit()

            print(f"Password updated successfully for user with ID {username} by admin.")
        else:
            print("Admin failed to update.")

    except Error as e:
        print(f"Error: {e}")


def delete_user_by_admin(conn,username):
    try:
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)
            delete_user_query = f"DELETE FROM users WHERE username = '{username}'"
            cursor.execute(delete_user_query)
            conn.commit()

            print(f"User with username {username} deleted successfully by admin.")
        else:
            print("Admin failed to delete.")

    except Error as e:
        print(f"Error: {e}")


def view_users(conn):
    try:
        cursor = conn.cursor(dictionary=True)

        view_users_query = "SELECT * FROM users"
        cursor.execute(view_users_query)
        users = cursor.fetchall()

        if users:
            print("User Data:")
            for user in users:
                print(f"Role: {user['role']}, Username: {user['username']}")
        else:
            print("No users found.")

    except Error as e:
        print(f"Error: {e}")
