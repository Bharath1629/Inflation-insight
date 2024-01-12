import mysql.connector
from tabulate import tabulate

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


def update_inflation_data(conn, country_code, year, new_energy_price, new_food_price, new_headline_price, new_core_price, new_producer_price):
    query = """
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
    data = (
        new_energy_price,
        new_food_price,
        new_headline_price,
        new_core_price,
        new_producer_price,
        country_code,
        year
    )
    with conn.cursor() as cursor:
        cursor.execute(query, data)
    conn.commit()
    print("Inflation data updated successfully.")

def view_country_data(conn):
    query = "SELECT * FROM countries"

    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(query)
        result = cursor.fetchall()

        if not result:
            print("No data found.")
            return

        data_tuples = [(row['country_code'], row['name'], row['IMF_count']) for row in result]
        headers = result[0].keys()
        print(tabulate(data_tuples, headers=headers, tablefmt="pretty"))