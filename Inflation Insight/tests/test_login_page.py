import unittest
from unittest.mock import MagicMock, patch
from login_page import new_user_registration
import mysql.connector
from mysql.connector import Error

class TestUserRegistration(unittest.TestCase):

    @patch('builtins.print')  # Mock the print function
    @patch('mysql.connector.connect')  # Mock the MySQL connection
    def test_new_user_registration(self, mock_connect, mock_print):
        # Mock the cursor and execute function
        mock_cursor = MagicMock()
        mock_cursor.execute.return_value = None

        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        # Test case 1: Successful registration
        new_user_registration(mock_conn, 'test_user', 'test_password')
        mock_cursor.execute.assert_called_once()  # Ensure execute is called
        mock_conn.commit.assert_called_once()     # Ensure commit is called
        mock_print.assert_any_call("Hi 'test_user', Thanks for registration!")

        # Test case 2: Error during registration
        mock_cursor.execute.side_effect = Error("Mocked database error")
        new_user_registration(mock_conn, 'error_user', 'error_password')
        mock_print.assert_any_call("Error: Mocked database error")

if __name__ == '__main__':
    unittest.main()
