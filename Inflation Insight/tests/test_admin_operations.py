import unittest
import mysql.connector
from unittest.mock import MagicMock
from admin_operations import *

class TestAdminOperations(unittest.TestCase):

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

    def test_authenticate_user(self):
        # Replace the following with a real username and password for testing
        username = "user"
        password = "12345"
        result = authenticate_user(self.conn, username, password)
        self.assertEqual(result, None)


    def test_create_user_by_admin(self):
        # Replace the following with test data for user creation
        username = "user2"
        password = "12345"
        role = "user"

        # Mocking cursor.execute to avoid actual database modification
        with unittest.mock.patch.object(self.conn.cursor(), 'execute', return_value=None):
            create_user_by_admin(self.conn, username, password, role)

        # Replace the following with a query to check if the user was created
        query = f"SELECT * FROM users WHERE username = '{username}'"
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            user = cursor.fetchone()

        self.assertIsNotNone(user)  # Check if the user was created in the database


    def test_update_user_by_admin(self):
        # Replace the following with test data for user update
        username = "abc"
        new_password = "xyz"

        # Mocking cursor.execute to avoid actual database modification
        with unittest.mock.patch.object(self.conn.cursor(), 'execute', return_value=None):
            update_user_by_admin(self.conn, username, new_password)

        # Replace the following with a query to check if the user was updated
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{new_password}'"
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            updated_user = cursor.fetchone()

        self.assertIsNotNone(updated_user)

    def test_delete_user_by_admin(self):
        # Replace the following with test data for user deletion
        username = "test_user"

        # Mocking cursor.execute to avoid actual database modification
        with unittest.mock.patch.object(self.conn.cursor(), 'execute', return_value=None):
            delete_user_by_admin(self.conn, username)

        # Replace the following with a query to check if the user was deleted
        query = f"SELECT * FROM users WHERE username = '{username}'"
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            deleted_user = cursor.fetchone()

        self.assertIsNone(deleted_user)

    def test_view_users(self):
        # Replace the following with test data for users
        test_users = [{'role': 'user', 'username': 'user1'}, {'role': 'admin', 'username': 'admin1'}]

        # Mocking cursor.execute to avoid actual database modification
        with unittest.mock.patch.object(self.conn.cursor(), 'execute', return_value=None):
            with unittest.mock.patch.object(self.conn.cursor(), 'fetchall', return_value=test_users):
                view_users(self.conn)

        # The test case should capture the printed output and check if it matches the expected output
        expected_output = "User Data:\nRole: user, Username: user1\nRole: admin, Username: admin1"
        with unittest.mock.patch("builtins.open", unittest.mock.mock_open(read_data=expected_output)):
            view_users(self.conn)


if __name__ == '__main__':
    unittest.main()
