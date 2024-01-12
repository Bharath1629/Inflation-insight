# crud_operations/crud_operations.py
import mysql.connector
from validation import *
from tabulate import *
def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Bharath 2001',
        database='projectinflation'
    )

def view_inflation_data(conn):
    query = "SELECT * FROM inflation LIMIT 10"
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        if not result:
            print("No data found.")
            return

        data_tuples = [(row['country_code'], row['year'], row['energy_consumer_price'], row['food_consumer_price'],row['headline_consumer_price'], row['official_core_consumer_price'], row['producer_price_inflation']) for row in result]
        headers = result[0].keys()
        print(tabulate(data_tuples, headers=headers, tablefmt="pretty"))


# crud_operations/crud_operations.py
def create_inflation_data(conn):
    country_code = validate_non_empty_input("Enter country code: ").upper()
    year = validate_numeric_input("Enter year: ")
    energy_price = validate_numeric_input("Enter Energy Consumer Price: ")
    food_price = validate_numeric_input("Enter Food Consumer Price: ")
    headline_price = validate_numeric_input("Enter Headline Consumer Price: ")
    core_price = validate_numeric_input("Enter Official Core Consumer Price: ")
    producer_price = validate_numeric_input("Enter Producer Price Inflation: ")

    query = """
        INSERT INTO inflation 
        (country_code, year, energy_consumer_price, food_consumer_price, headline_consumer_price, official_core_consumer_price, producer_price_inflation) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (
        country_code,
        year,
        energy_price,
        food_price,
        headline_price,
        core_price,
        producer_price
    )
    with conn.cursor() as cursor:
        cursor.execute(query, data)
    conn.commit()
    print("Inflation data created successfully.")



def update_inflation_data(conn):
    # country_code, year, new_energy_price, new_food_price, new_headline_price, new_core_price, new_producer_price):
    # Check if the data exists before updating
    country_code = validate_non_empty_input("Enter country code: ").upper()
    year = validate_numeric_input("Enter year: ")
    energy_consumer_price = validate_numeric_input("Enter Energy Consumer Price: ")
    food_consumer_price = validate_numeric_input("Enter Food Consumer Price: ")
    headline_consumer_price = validate_numeric_input("Enter Headline Consumer Price: ")
    official_core_consumer_price = validate_numeric_input("Enter Official Core Consumer Price: ")
    producer_price_inflation = validate_numeric_input("Enter Producer Price Inflation: ")
    check_query = """
        SELECT COUNT(*) 
        FROM inflation 
        WHERE country_code = %s AND year = %s
    """
    check_data = (country_code, year)

    with conn.cursor() as check_cursor:
        check_cursor.execute(check_query, check_data)
        result = check_cursor.fetchone()

    if result[0] == 0:
        print(f"Inflation data not found for country code {country_code} and year {year}. Please provide correct data.")
        year = validate_numeric_input("Enter year: ")

# If data exists, proceed with the update
    update_query = """
        UPDATE inflation 
        SET 
            energy_consumer_price = %s,
            food_consumer_price = %s,
            headline_consumer_price = %s,
            official_core_consumer_price = %s,
            producer_price_inflation = %s
        WHERE 
            country_code = %s AND 
            year = %s
    """
    update_data = (
        energy_consumer_price,
        food_consumer_price,
        headline_consumer_price,
        official_core_consumer_price,
        producer_price_inflation,
        country_code,
        year
    )

    with conn.cursor() as update_cursor:
        update_cursor.execute(update_query, update_data)

    conn.commit()
    print("Inflation data updated successfully.")

def delete_inflation_data(conn, country_code, year):
    check_query = """
        SELECT COUNT(*) 
        FROM inflation 
        WHERE country_code = %s AND year = %s
    """
    check_data = (country_code, year)
    with conn.cursor() as check_cursor:
        check_cursor.execute(check_query, check_data)
        result = check_cursor.fetchone()

    if result[0] == 0:
        print(f"Inflation data not found for country code {country_code} and year {year}. Please provide correct data.")
        delete_inflation_data(conn, input("Enter country to delete: "), input("Enter year to delete: "))

    query = "DELETE FROM inflation WHERE country_code = %s AND year = %s"
    data = (country_code, year)
    with conn.cursor() as cursor:
        cursor.execute(query, data)
    conn.commit()
    print("Inflation data deleted successfully.")
