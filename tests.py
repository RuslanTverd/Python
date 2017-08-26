import unittest
from main.kalkulator import plus, minus, multiply, division

class TestStringMethods(unittest.TestCase):
	def test_plus(self):
		assert plus(2,2) == 4

	def test_minus(self):
		assert minus(4,2) == 2

	def test_multiply(self):
		assert multiply(3,3) == 9

	def test_division(self):
		assert division(8,2) == 4

if __name__ == '__main__':
	unittest.main()
