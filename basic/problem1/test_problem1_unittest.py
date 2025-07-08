import unittest
from unittest.mock import patch
from io import StringIO
from problem1 import main

class TestProblem1(unittest.TestCase):

    @patch('builtins.input', side_effect=["5", "2 5 9 6 1", "0"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_pares(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "2 6")

    @patch('builtins.input', side_effect=["5", "2 5 9 6 1", "1"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_impares(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "5 9 1")

if __name__ == '__main__':
    unittest.main()
