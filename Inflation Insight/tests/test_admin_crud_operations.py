
import unittest
from unittest.mock import patch
from io import StringIO
from admin_crud_operations import *

class TestInflationCRUDOperations(unittest.TestCase):

    def setUp(self):
        # Create a connection to an in-memory database for testing
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Bharath 2001',
            database='projectinflation'
        )

    def tearDown(self):
        # Close the connection after each test
        self.conn.close()

    def test_view_inflation_data(self):
        # Assuming you have some test data in the database
        # Create the necessary table and insert some test data

        # Redirect stdout to capture the print output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            view_inflation_data(self.conn)

        # Assert that the output contains the expected table headers
        self.assertIn("country_code", mock_stdout.getvalue())

    def test_create_inflation_data(self):
        # Redirect user input to provide test data
        with patch('builtins.input', side_effect=['USA', '2025', '1.5', '2.5', '3.5', '4.5', '5.5']):
            create_inflation_data(self.conn)

        # Check if the data was inserted into the database
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM inflation WHERE country_code = 'USA' AND year = 2010")
            result = cursor.fetchone()
            self.assertIsNotNone(result)

    def test_update_inflation_data(self):
        # Assuming you have some existing data in the database
        # Redirect user input to provide test data
        with patch('builtins.input', side_effect=['USA', '2010', '1.5', '2.5', '3.5', '4.5', '5.5']):
            update_inflation_data(self.conn)

        # Check if the data was updated in the database
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM inflation WHERE country_code = 'USA' AND year = 2010")
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result['energy_consumer_price'], 1.5)

    def test_delete_inflation_data(self):
        # Assuming you have some existing data in the database
        # Redirect user input to provide test data
        with patch('builtins.input', side_effect=['USA', '2025']):
            delete_inflation_data(self.conn, 'USA', '2025')

        # Check if the data was deleted from the database
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM inflation WHERE country_code = 'USA' AND year = 2025")
            result = cursor.fetchone()
            self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
