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