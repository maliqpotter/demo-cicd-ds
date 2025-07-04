import unittest
from app import Calculator, greet


class TestCalculator(unittest.TestCase):
    """Test class untuk Calculator"""

    def setUp(self):
        """Setup untuk setiap test"""
        self.calc = Calculator()

    def test_add(self):
        """Test fungsi add"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtract(self):
        """Test fungsi subtract"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(10.5, 5.5), 5.0)

    def test_multiply(self):
        """Test fungsi multiply"""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_divide(self):
        """Test fungsi divide"""
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_divide_by_zero(self):
        """Test pembagian dengan nol harus raise ValueError"""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

        with self.assertRaises(ValueError):
            self.calc.divide(-3, 0)


class TestGreet(unittest.TestCase):
    """Test class untuk fungsi greet"""

    def test_greet_with_name(self):
        """Test greet dengan nama"""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")
        self.assertEqual(greet("CI/CD"), "Hello, CI/CD!")

    def test_greet_without_name(self):
        """Test greet tanpa nama"""
        self.assertEqual(greet(""), "Hello, World!")
        self.assertEqual(greet(None), "Hello, World!")


if __name__ == "__main__":
    # Menjalankan semua tests
    unittest.main(verbosity=2)
