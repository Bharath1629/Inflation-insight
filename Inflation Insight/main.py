# main.py
import mysql.connector
from mysql.connector import Error
import csv
from crud_operations import *
from user_operations import authenticate_user
from menu import display_menu, handle_menu_choice

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
def load_data_from_csv(conn, csv_path, table_name):
    cursor = conn.cursor()
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            placeholders = ', '.join(['%s' for _ in row])
            cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', row)
    conn.commit()
    print(f"Data loaded into '{table_name}' table successfully.")

def main():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Bharath 2001',
        )

        cursor = conn.cursor()

        # Create the database
        #create_database(cursor)

        # Switch to the 'projectinflation' database
        cursor.execute("USE projectinflation;")

#         # Create tables
#         create_tables(conn)
#
#         # Load data from CSV files
#         load_data_from_csv(conn, 'C:/Users/91630/Desktop/Revature/users.csv', 'users')
#         load_data_from_csv(conn, 'C:/Users/91630/Desktop/Revature/countries.csv', 'countries')
#         load_data_from_csv(conn, 'C:/Users/91630/Desktop/Revature/inflation.csv', 'inflation')

        user = authenticate_user(conn, input("Enter username: "), input("Enter password: "))

        if user:
            while True:
                display_menu()
                choice = input("Enter your choice: ")

                if choice == '5':
                    break

                handle_menu_choice(choice, conn, user)


    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    main()
