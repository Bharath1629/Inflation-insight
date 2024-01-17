import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from main import main

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'admin1', 'admin1', '9'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_admin_login_and_exit(self, mock_stdout, mock_input):
        main()
        expected_output = "1. Admin user\n2. Normal user\n3. New user\n+--------------------------+\n| 1. View Inflation Data   |\n| 2. Create Inflation Data |\n| 3. Update Inflation Data |\n| 4. Delete Inflation Data |\n| 5. Create new user       |\n| 6. Update user details   |\n| 7. Delete user           |\n| 8. View users data       |\n| 9. Exit                  |\n+--------------------------+\nThanks for your time! See you again!\nMySQL connection closed.\n"
        self.assertEqual(expected_output.strip(), mock_stdout.getvalue().strip())

    @patch('builtins.input', side_effect=['1', 'fgerf', 'admi', '1','admin1','admin1','9'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_admin_invalid_login_and_exit(self, mock_stdout, mock_input):
        main()
        expected_output = "1. Admin user\n2. Normal user\n3. New user\nEnter valid credentials!\n1. Admin user\n2. Normal user\n3. New user\n+--------------------------+\n| 1. View Inflation Data   |\n| 2. Create Inflation Data |\n| 3. Update Inflation Data |\n| 4. Delete Inflation Data |\n| 5. Create new user       |\n| 6. Update user details   |\n| 7. Delete user           |\n| 8. View users data       |\n| 9. Exit                  |\n+--------------------------+\nThanks for your time! See you again!\nMySQL connection closed.\n"
        self.assertEqual(expected_output.strip(), mock_stdout.getvalue().strip())

    @patch('builtins.input', side_effect=['admin1','1','admin1','admin1','9'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_choice(self, mock_stdout, mock_input):
        main()
        expected_output = "1. Admin user\n2. Normal user\n3. New user\nPlease, Enter valid number!\n1. Admin user\n2. Normal user\n3. New user\n+--------------------------+\n| 1. View Inflation Data   |\n| 2. Create Inflation Data |\n| 3. Update Inflation Data |\n| 4. Delete Inflation Data |\n| 5. Create new user       |\n| 6. Update user details   |\n| 7. Delete user           |\n| 8. View users data       |\n| 9. Exit                  |\n+--------------------------+\nThanks for your time! See you again!\nMySQL connection closed.\n"
        self.assertEqual(expected_output.strip(), mock_stdout.getvalue().strip())

    @patch('builtins.input', side_effect=['2','dfbg','sdfg','2','user1','12345','5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_user_invalid_login_and_exit(self, mock_stdout, mock_input):
        main()
        expected_output = "1. Admin user\n2. Normal user\n3. New user\nEnter valid credentials!\n1. Admin user\n2. Normal user\n3. New user\n+-------------------------------------+\n| 1. View data of inflation           |\n| 2. View Country data                |\n| 3. Analysis Operations on Inflation |\n| 4. Analysis on Country Data         |\n| 5. Exit                             |\n+-------------------------------------+\nThanks for your time!\nMySQL connection closed.\n"
        self.assertEqual(expected_output.strip(), mock_stdout.getvalue().strip())

    @patch('builtins.input', side_effect=['3','user1','12345','abc','xyz','5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_user_invalid_login_and_exit(self, mock_stdout, mock_input):
        main()
        expected_output = "1. Admin user\n2. Normal user\n3. New user\nError: 1062 (23000): Duplicate entry 'user1' for key 'users.PRIMARY'\n+-------------------------------------+\n| 1. View data of inflation           |\n| 2. View Country data                |\n| 3. Analysis Operations on Inflation |\n| 4. Analysis on Country Data         |\n| 5. Exit                             |\n+-------------------------------------+\nThanks for your time!\nMySQL connection closed.\n"
        self.assertEqual(expected_output.strip(), mock_stdout.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
