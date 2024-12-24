import unittest
from calculator import calc, is_number


class CalculatorTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(calc('3 + 4 - 1'), 6.0)

    def test_2(self):
        self.assertEqual(calc('3 * 4 * 10-15/2'), 112.5)

    def test_3(self):
        self.assertEqual(calc('3 / 4'), 0.75)

    def test_4(self):
        self.assertEqual(calc('3//4 = 0'), 'ERROR')

    def test_5(self):
        self.assertEqual(calc('-1-1-1'), -3.0)

    def test_6(self):
        self.assertEqual(calc('8**190-1--1'), 'ERROR')

    def test_7(self):
        self.assertEqual(calc('3.5 + 4.'), 7.5)

    def test_8(self):
        self.assertEqual(calc('17 + 1 / 0'), 'ERROR')

    def test_9(self):
        self.assertEqual(calc('10 + 0  '), 10)

    def test_10(self):
        self.assertEqual(calc(' '), 'ERROR')

    def test_11(self):
        self.assertEqual(calc('lol + lol'), 'ERROR')

if __name__ == '__main__':
    unittest.main()
