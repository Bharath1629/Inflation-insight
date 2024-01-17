import unittest
import mysql.connector
from unittest.mock import MagicMock, patch
import pandas as pd
from users_operations import analysis_operations_inflation, analysis_country_data

class TestAnalysisOperations(unittest.TestCase):

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

    @patch('seaborn.barplot')
    def test_analysis_operations_inflation(self, mock_barplot):
        # Replace the following with test data for the inflation table
        test_data = [{'year': 2021, 'energy_consumer_price': 2.5, 'food_consumer_price': 1.8},
                     {'year': 2022, 'energy_consumer_price': 3.0, 'food_consumer_price': 2.0}]

        # Mocking cursor.execute and cursor.fetchall to avoid actual database modification
        with unittest.mock.patch.object(self.conn.cursor(), 'execute', return_value=None):
            with unittest.mock.patch.object(self.conn.cursor(), 'fetchall', return_value=test_data):
                analysis_operations_inflation(self.conn, 'USA')

        mock_barplot.assert_called()

    @patch('seaborn.barplot')
    def test_analysis_country_data(self, mock_barplot):
        # Replace the following with test data for the countries table
        test_data = [{'name': 'United States', 'IMF_count': 1, 'country_code': 'USA'},
                     {'name': 'India', 'IMF_count': 2, 'country_code': 'IND'}]

        # Mocking cursor.execute and cursor.fetchall to avoid actual database modification
        with unittest.mock.patch.object(self.conn.cursor(), 'execute', return_value=None):
            with unittest.mock.patch.object(self.conn.cursor(), 'fetchall', return_value=test_data):
                analysis_country_data(self.conn, ['USA', 'IND'])

        mock_barplot.assert_called()

if __name__ == '__main__':
    unittest.main()
