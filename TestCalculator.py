#write unit tests to validate positive and negative conditions
#of Calculator.py
import unittest
from Calculator import add, subtract, multiply, divide, modulus, exponent, floor_division, calculator,fn_generate_random
class TestCalculator(unittest.TestCase):

    def test_validate_Random(self):
        """Test the random number generation function."""
        seed_value = 900
        expected_random_number = 866  # This value should be determined based on the seed
        self.assertEqual(fn_generate_random(seed_value), expected_random_number)


    def test_add(self):
        self.assertEqual(add(2, 3),  5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertRaises(ValueError, divide, 5, 0)

    def test_modulus(self):
        self.assertEqual(modulus(5, 3), 2)
        self.assertEqual(modulus(5, 5), 0)

    def test_exponent(self):
        self.assertEqual(exponent(2, 3), 8)
        self.assertEqual(exponent(5, 0), 1)

    def test_floor_division(self):
        self.assertEqual(floor_division(7, 3), 2)
        self.assertRaises(ValueError, floor_division, 5, 0)

    def test_calculator(self):
        self.assertEqual(calculator(4,4,'multiply'),16)
        self.assertEqual(calculator(2, 3, 'add'), 5)
        self.assertEqual(calculator(5, 3, 'subtract'), 2)
        self.assertEqual(calculator(4, 2, 'multiply'), 8)
        self.assertEqual(calculator(6, 3, 'divide'), 2.0)
        self.assertRaises(ValueError, calculator, 5, 0, 'divide')
        self.assertEqual(calculator(10, 3, 'modulus'), 1)
        self.assertEqual(calculator(2, 3, 'exponent'), 8)
        self.assertRaises(ValueError, calculator, 5, 0, 'floor_division')
        self.assertEqual(calculator(7, 3, 'floor_division'), 2)
    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculator(2, 3, 'invalid_operation')
if __name__ == '__main__':
    unittest.main()
# Unit tests for the calculator functions
# This code defines a set of unit tests for the calculator functions in Calculator.py.
# It uses the unittest framework to validate both positive and negative conditions.
# The tests cover all operations including addition, subtraction, multiplication, division,
# modulus, exponentiation, and floor division. It also tests the calculator function
# to ensure it correctly routes operations and handles invalid inputs.
# The tests are designed to ensure that the calculator functions behave as expected
# and raise appropriate exceptions when necessary.
# This code defines a set of unit tests for the calculator functions in Calculator.py.
# It uses the unittest framework to validate both positive and negative conditions.


