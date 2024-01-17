import unittest
from unittest.mock import patch, MagicMock
from menu_for_admin import *

class TestMenuFunctions(unittest.TestCase):

    @patch('menu_for_admin.view_inflation_data')
    def test_handle_menu_choice_view_data(self, mock_view_inflation_data):
        conn = MagicMock()
        handle_menu_choice('1', conn)
        mock_view_inflation_data.assert_called_once_with(conn)

    @patch('menu_for_admin.create_inflation_data')
    def test_handle_menu_choice_create_data(self, mock_create_inflation_data):
        conn = MagicMock()
        handle_menu_choice('2', conn)
        mock_create_inflation_data.assert_called_once_with(conn)

    @patch('menu_for_admin.update_inflation_data')
    def test_handle_menu_choice_update_data(self, mock_update_inflation_data):
        conn = MagicMock()
        handle_menu_choice('3', conn)
        mock_update_inflation_data.assert_called_once_with(conn)

    @patch('menu_for_admin.delete_inflation_data')
    @patch('builtins.input', side_effect=['country', 'year'])
    def test_handle_menu_choice_delete_data(self, mock_input, mock_delete_inflation_data):
        conn = MagicMock()
        handle_menu_choice('4', conn)
        mock_input.assert_has_calls([unittest.mock.call("Enter country to delete: "), unittest.mock.call("Enter year to delete: ")])
        mock_delete_inflation_data.assert_called_once_with(conn, 'country', 'year')

    @patch('builtins.print')
    def test_handle_menu_choice_exit(self, mock_print):
        conn = MagicMock()
        handle_menu_choice('9', conn)
        mock_print.assert_called_once_with("Exiting. Goodbye!")

    @patch('menu_for_admin.create_user_by_admin')
    @patch('builtins.input', side_effect=['name', 'password', 'role'])
    def test_handle_menu_choice_create_user(self, mock_input, mock_create_user_by_admin):
        conn = MagicMock()
        handle_menu_choice('5', conn)
        mock_input.assert_has_calls([unittest.mock.call("Enter the name of new user: "), unittest.mock.call("Enter password for user: "), unittest.mock.call("Enter user role: ")])
        mock_create_user_by_admin.assert_called_once_with(conn, 'name', 'password', 'role')

    @patch('menu_for_admin.update_user_by_admin')
    @patch('builtins.input', side_effect=['username', 'new_password'])
    def test_handle_menu_choice_update_user(self, mock_input, mock_update_user_by_admin):
        conn = MagicMock()
        handle_menu_choice('6', conn)
        mock_input.assert_has_calls([unittest.mock.call("Enter username: "), unittest.mock.call("Enter new password: ")])
        mock_update_user_by_admin.assert_called_once_with(conn, 'username', 'new_password')

    @patch('menu_for_admin.delete_user_by_admin')
    @patch('builtins.input', return_value='username')
    def test_handle_menu_choice_delete_user(self, mock_input, mock_delete_user_by_admin):
        conn = MagicMock()
        handle_menu_choice('7', conn)
        mock_input.assert_called_once_with("Enter username: ")
        mock_delete_user_by_admin.assert_called_once_with(conn, 'username')

    @patch('menu_for_admin.view_users')
    def test_handle_menu_choice_view_users(self, mock_view_users):
        conn = MagicMock()
        handle_menu_choice('8', conn)
        mock_view_users.assert_called_once_with(conn)

    @patch('builtins.print')
    def test_handle_menu_choice_invalid_choice(self, mock_print):
        conn = MagicMock()
        handle_menu_choice('invalid', conn)
        mock_print.assert_called_once_with("Invalid choice. Try again.")

if __name__ == '__main__':
    unittest.main()
