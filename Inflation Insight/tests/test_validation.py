import unittest
from unittest.mock import patch
from validation import validate_non_empty_input, validate_numeric_input

class TestValidationFunctions(unittest.TestCase):

    @patch('builtins.input', return_value='Test Value')
    def test_validate_non_empty_input_valid(self, mock_input):
        result = validate_non_empty_input("Enter a value: ")
        self.assertEqual(result, 'Test Value')

    @patch('builtins.input', side_effect=['', '', 'Non-Empty Value'])
    def test_validate_non_empty_input_multiple_attempts(self, mock_input):
        result = validate_non_empty_input("Enter a value: ")
        self.assertEqual(result, 'Non-Empty Value')

    # @patch('builtins.input', return_value='Not a Number')
    # def test_validate_numeric_input_invalid_input(self, mock_input):
    #     result = validate_numeric_input("Enter a numeric value: ")
    #     self.assertIsNone(result)  # In this case, the function returns None for an invalid input

    @patch('builtins.input', return_value='42.5')
    def test_validate_numeric_input_valid_input(self, mock_input):
        result = validate_numeric_input("Enter a numeric value: ")
        self.assertEqual(result, 42.5)

    @patch('builtins.input', side_effect=['abc', '23.5'])
    def test_validate_numeric_input_multiple_attempts(self, mock_input):
        result = validate_numeric_input("Enter a numeric value: ")
        self.assertEqual(result, 23.5)

if __name__ == '__main__':
    unittest.main()
