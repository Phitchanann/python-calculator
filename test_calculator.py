import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    # add(): 2 test cases
    def test_add_positive(self):
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-3, -4), -7)

    # subtract(): 2 test cases
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    # multiply(): 2 test cases
    def test_multiply_basic(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # divide(): 2 test cases
    def test_divide_exact(self):
        self.assertEqual(self.calc.divide(20, 5), 4)

    def test_divide_no_fraction(self):
        self.assertEqual(self.calc.divide(7, 2), 3)

    # modulo(): 2 test cases
    def test_modulo_basic(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_zero_result(self):
        self.assertEqual(self.calc.modulo(8, 4), 0)

if __name__ == '__main__':
    unittest.main()

