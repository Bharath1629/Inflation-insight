# main.py
import mysql.connector
from mysql.connector import Error
import csv
from admin_crud_operations import *
from admin_operations import authenticate_user
from menu_for_admin import display_menu, handle_menu_choice
from menu_for_user import *
from login_page import *

# def create_database(cursor):
#     try:
#         cursor.execute("CREATE DATABASE IF NOT EXISTS projectinflation;")
#         print("Database 'projectinflation' created successfully.")
#     except Error as e:
#         print(f"Error creating database: {e}")
#
# def create_tables(conn):
#     cursor = conn.cursor()
#
#     # Create 'users' table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             username VARCHAR(255) PRIMARY KEY,
#             password VARCHAR(255) NOT NULL,
#             role VARCHAR(255) NOT NULL
#         );
#     ''')
#
#     # Create 'countries' table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS countries (
#             country_code VARCHAR(255) PRIMARY KEY,
#             name VARCHAR(255) NOT NULL,
#             IMF_count INTEGER NOT NULL
#         );
#     ''')
#
#     # Create 'inflation' table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS inflation (
#             record_id INT AUTO_INCREMENT PRIMARY KEY,
#             country_code VARCHAR(255),
#             year INT,
#             energy_consumer_price FLOAT,
#             food_consumer_price FLOAT,
#             headline_consumer_price FLOAT,
#             official_core_consumer_price FLOAT,
#             producer_price_inflation FLOAT,
#             FOREIGN KEY (country_code) REFERENCES countries(country_code)
#         );
#     ''')
#
#     conn.commit()
#     print("Tables created successfully.")
#
# def load_data_from_csv(conn, csv_path, table_name):
#     cursor = conn.cursor()
#     with open(csv_path, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for row in reader:
#             placeholders = ', '.join(['%s' for _ in row])
#             cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', row)
#     conn.commit()
#     print(f"Data loaded into '{table_name}' table successfully.")

def main():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Bharath 2001',
        )

        cursor = conn.cursor()


        # Switch to the 'projectinflation' database
        cursor.execute("USE projectinflation;")

#         # Create tables
#         create_tables(conn)
#         # Load data from CSV files
#         load_data_from_csv(conn, 'C:/Users/91630/Desktop/Revature/users.csv', 'users')
#         load_data_from_csv(conn, 'C:/Users/91630/Desktop/Revature/countries.csv', 'countries')
#         load_data_from_csv(conn, 'C:/Users/91630/Desktop/Revature/inflation.csv', 'inflation')
        while (True):
            display_login()
            choice=input("Enter your choice: ")
            if choice=='1':
                user = authenticate_user(conn, input("Enter username: "), input("Enter password: "),'admin')
                if not user:
                    print("Enter valid credentials!")
                    continue
                while True:
                    display_menu()
                    choice = input("Enter your choice: ")

                    if choice == '9':
                        print("Thanks for your time! See you again!")
                        break

                    handle_menu_choice(choice, conn)
                break
            elif choice=='2':
                user = authenticate_user(conn, input("Enter username: "), input("Enter password: "),'user')
                if not user:
                    print("Enter valid credentials!")
                    continue
                while True:
                    display_user_menu()
                    choice=input("Enter your choice: ")
                    if choice=='5':
                        print("Thanks for your time!")
                        break
                    handle_menu_user_choice(choice, conn)
                break
            elif choice=='3':
                new_user_registration(conn,input("Enter username: "),input("Enter password: "))
                user = authenticate_user(conn, input("Enter username: "), input("Enter password: "),'user')
                if not user:
                    print("Enter valid credentials!")
                    continue
                while True:
                    display_user_menu()
                    choice=input("Enter your choice: ")
                    if choice=='5':
                        print("Thanks for your time!")
                        break
                    handle_menu_user_choice(choice, conn)
                break
            else:
                print("Please, Enter valid number!")


    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    main()
