# menu.py
from crud_operations import *

def display_menu():
    print("1. View Inflation Data")
    print("2. Create Inflation Data")
    print("3. Update Inflation Data")
    print("4. Delete Inflation Data")
    print("5. Exit")

def handle_menu_choice(choice, conn, user):
    if user['role'] == 'admin':
        if choice == '1':
            view_inflation_data(conn)
        elif choice == '2':
            create_inflation_data(conn, input("Enter country: "), input("Enter year: "), input("Enter Energy Consumer Price: "), input("Enter Food Consumer Price: "), input("Enter Headline Consumer Price: "), input("Enter Official Core Consumer Price: "), input("Enter Producer Price Inflation: "))
        elif choice == '3':
            update_inflation_data(conn, input("Enter country to update: "), input("Enter year to update: "), input("Enter new Energy Consumer Price: "), input("Enter new Food Consumer Price: "), input("Enter new Headline Consumer Price: "), input("Enter new Official Core Consumer Price: "), input("Enter new Producer Price Inflation: "))
        elif choice == '4':
            delete_inflation_data(conn, input("Enter country to delete: "), input("Enter year to delete: "))
        elif choice == '5':
            print("Exiting. Goodbye!")
        else:
            print("Invalid choice. Try again.")
    elif user['role'] == 'user':
        if choice == '1':
            view_inflation_data(conn)
        elif choice == '3':
            update_inflation_data(conn, input("Enter country to update: "), input("Enter year to update: "), input("Enter new Energy Consumer Price: "), input("Enter new Food Consumer Price: "), input("Enter new Headline Consumer Price: "), input("Enter new Official Core Consumer Price: "), input("Enter new Producer Price Inflation: "))
        elif choice == '5':
            print("Exiting. Goodbye!")
        else:
            print("Invalid choice. Try again.")
    else:
        print("Invalid user role. Exiting.")
