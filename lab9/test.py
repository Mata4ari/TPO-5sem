import unittest
from unittest.mock import patch
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.cl = Calculator(5)
        

    @patch.object(Calculator, 'minus', return_value=Calculator(4))
    def test_plus(self, mock):
        result = self.cl.minus(1).plus(5).count
        mock.assert_called_once_with(1)
        self.assertEqual(result, 9)

    @patch.object(Calculator, 'plus', return_value=Calculator(10))
    def test_withdraw(self, mock):
        result = self.cl.plus(5).minus(1).count
        mock.assert_called_once_with(5)
        self.assertEqual(result, 9)


