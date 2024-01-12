from user_crud_operations import *
from users_operations import *

def display_user_menu():
    print("+-------------------------------------+")
    print("| 1. View data of inflation           |")
    print("| 2. Update the inflation data        |")
    print("| 3. View Country data                |")
    print("| 4. Analysis Operations on Inflation |")
    print("| 5. Analysis on Country Data         |")
    print("| 6. Exit                             |")
    print("+-------------------------------------+")



def handle_menu_user_choice(choice,conn):
    if choice=='1':
        view_inflation_data(conn)
    elif choice=='2':
        update_inflation_data(conn, input("Enter country to update: "), input("Enter year to update: "), input("Enter new Energy Consumer Price: "), input("Enter new Food Consumer Price: "), input("Enter new Headline Consumer Price: "), input("Enter new Official Core Consumer Price: "), input("Enter new Producer Price Inflation: "))
    elif choice=='3':
        view_country_data(conn)
    elif choice=='4':
        analysis_operations_inflation(conn,input("Enter country code: "))
    elif choice=='5':
        codes=get_multiple_inputs()
        analysis_country_data(conn,codes)
    else:
        print("Invalid Choice, Try again!")