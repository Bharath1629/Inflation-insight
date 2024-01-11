# crud_operations/crud_operations.py
import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Bharath 2001',
        database='projectinflation'
    )

def view_inflation_data(conn):
    query = "SELECT * FROM inflation"
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)

def create_inflation_data(conn, country_code, year, energy_price, food_price, headline_price, core_price, producer_price):
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

def delete_inflation_data(conn, country_code, year):
    query = "DELETE FROM inflation WHERE country_code = %s AND year = %s"
    data = (country_code, year)
    with conn.cursor() as cursor:
        cursor.execute(query, data)
    conn.commit()
    print("Inflation data deleted successfully.")
