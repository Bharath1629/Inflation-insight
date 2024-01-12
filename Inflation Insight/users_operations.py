import mysql.connector
from mysql.connector import Error
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def analysis_operations_inflation(conn, country_code):
    query = "SELECT country_code, year, energy_consumer_price, food_consumer_price, headline_consumer_price, official_core_consumer_price, producer_price_inflation FROM inflation WHERE country_code = %s"
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(query, (country_code,))
        result = cursor.fetchall()

    inflation_data = result
    df_inflation = pd.DataFrame(inflation_data)

    if df_inflation.empty:
        print(f"No data found for country code {country_code}")
    else:
        col_data = ['energy_consumer_price', 'food_consumer_price', 'headline_consumer_price', 'official_core_consumer_price', 'producer_price_inflation']

        # Melt the DataFrame to combine columns into a single variable
        df_melted = pd.melt(df_inflation, id_vars=['year'], value_vars=col_data, var_name='Consumer Price Type', value_name='Consumer Price')

        plt.figure(figsize=(12, 6))
        sns.barplot(x="year", y="Consumer Price", hue="Consumer Price Type", data=df_melted, palette="viridis")
        plt.xlabel("Year")
        plt.ylabel("Consumer Price")
        plt.title(f"Bar Graph for Consumer Prices in {country_code}")
        plt.legend(title="Consumer Price Type", bbox_to_anchor=(1, 1))
        plt.show()

def analysis_country_data(conn, country_codes):
    # Convert the list of country codes to uppercase
    country_codes_upper = [code.upper() for code in country_codes]

    # Generate placeholders for the IN clause
    placeholders = ', '.join(['%s'] * len(country_codes_upper))

    query = f"SELECT name, IMF_count, country_code FROM COUNTRIES WHERE COUNTRY_CODE IN ({placeholders})"
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(query, country_codes_upper)
        result = cursor.fetchall()

    inflation_country_data = result
    df_inflation_country = pd.DataFrame(inflation_country_data)

    if df_inflation_country.empty:
        print("No data found for the provided country codes")
    else:
        plt.figure(figsize=(12, 6))
        sns.barplot(x="name", y="IMF_count", hue="country_code", data=df_inflation_country, palette="viridis")
        plt.xlabel("Country")
        plt.ylabel("IMF count")
        plt.title("Bar Graph for IMF Count in Selected Countries")
        plt.legend(title="Country Code", bbox_to_anchor=(1, 1))
        plt.show()

def get_multiple_inputs():
    user_inputs = []
    while True:
        user_input = input("Enter a country code (or 'done' to finish): ").upper()  # Convert to uppercase for consistency
        if user_input == 'DONE':
            break
        user_inputs.append(user_input)
    return user_inputs

