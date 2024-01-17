from user_crud_operations import *
from users_operations import *

def display_user_menu():
    print("+-------------------------------------+")
    print("| 1. View data of inflation           |")
    print("| 2. View Country data                |")
    print("| 3. Analysis Operations on Inflation |")
    print("| 4. Analysis on Country Data         |")
    print("| 5. Exit                             |")
    print("+-------------------------------------+")



def handle_menu_user_choice(choice,conn):
    if choice=='1':
        view_inflation_data(conn)
    elif choice=='2':
        view_country_data(conn)
    elif choice=='3':
        analysis_operations_inflation(conn,input("Enter country code: "))
    elif choice=='4':
        codes=get_multiple_inputs()
        analysis_country_data(conn,codes)
    else:
        print("Invalid Choice, Try again!")