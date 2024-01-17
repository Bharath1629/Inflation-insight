import unittest
import mysql.connector
from unittest.mock import MagicMock
from user_crud_operations import view_inflation_data, view_country_data

class TestViewFunctions(unittest.TestCase):

    def setUp(self):
        # Replace the following with your actual database connection details for testing
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bharath 2001",
            database="projectinflation"
        )

    def tearDown(self):
        if self.conn.is_connected():
            self.conn.close()

    def test_view_inflation_data(self):
        # Replace the following with test data for the inflation table
        test_data = [{'country_code': 'USA', 'year': 2021, 'energy_consumer_price': 2.5, 'food_consumer_price': 1.8},
                     {'country_code': 'IND', 'year': 2021, 'energy_consumer_price': 3.0, 'food_consumer_price': 2.0}]

        # Mocking cursor.execute and cursor.fetchall to avoid actual database modification
        with unittest.mock.patch.object(self.conn.cursor(), 'execute', return_value=None):
            with unittest.mock.patch.object(self.conn.cursor(), 'fetchall', return_value=test_data):
                view_inflation_data(self.conn)

    def test_view_country_data(self):
        # Replace the following with test data for the countries table
        test_data = [{'country_code': 'USA', 'name': 'United States', 'IMF_count': 1},
                     {'country_code': 'IND', 'name': 'Canada', 'IMF_count': 2}]

        # Mocking cursor.execute and cursor.fetchall to avoid actual database modification
        with unittest.mock.patch.object(self.conn.cursor(), 'execute', return_value=None):
            with unittest.mock.patch.object(self.conn.cursor(), 'fetchall', return_value=test_data):
                view_country_data(self.conn)

if __name__ == '__main__':
    unittest.main()
