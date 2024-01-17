import unittest
from unittest.mock import patch, MagicMock
from user_crud_operations import *
from menu_for_user import *

class TestUserMenu(unittest.TestCase):

    @patch('builtins.print')
    def test_display_user_menu(self, mock_print):
        display_user_menu()
        mock_print.assert_called_with("+-------------------------------------+")

    @patch('menu_for_user.input', side_effect=['1'])
    @patch('menu_for_user.view_inflation_data')
    def test_handle_menu_user_choice_view_inflation_data(self, mock_view_inflation_data, mock_input):
        handle_menu_user_choice('1', MagicMock())
        mock_view_inflation_data.assert_called_once()


    @patch('menu_for_user.input', side_effect=['2'])
    @patch('menu_for_user.view_country_data')
    def test_handle_menu_user_choice_view_country_data(self, mock_view_country_data, mock_input):
        handle_menu_user_choice('2', MagicMock())
        mock_view_country_data.assert_called_once()

    # @patch('menu_for_user.input', side_effect=['3', 'USA'])
    # @patch('menu_for_user.analysis_operations_inflation')
    # def test_handle_menu_user_choice_analysis_operations_inflation(self, mock_analysis_operations_inflation, mock_input):
    #     handle_menu_user_choice('3', MagicMock())
    #     mock_analysis_operations_inflation.assert_called_once_with(MagicMock(), 'USA')
    #
    # @patch('menu_for_user.input', side_effect=['4', 'USA', 'SSD', 'IND','done'])
    # @patch('menu_for_user.analysis_country_data')
    # def test_handle_menu_user_choice_analysis_country_data(self, mock_analysis_country_data, mock_input):
    #     handle_menu_user_choice('4', MagicMock())
    #     mock_analysis_country_data.assert_called_once_with(MagicMock(), ['USA', 'SSD', 'IND'])

    @patch('builtins.print')
    def test_handle_menu_user_choice_invalid_choice(self, mock_print):
        handle_menu_user_choice('invalid_choice', MagicMock())
        mock_print.assert_called_with("Invalid Choice, Try again!")

if __name__ == '__main__':
    unittest.main()
