import unittest
from main.kalkulator1 import fnom2, fstroka, fz

class TestStringMethods(unittest.TestCase):
	def test_fnom2(self):
		assert fnom2(1,"1+1+1") == 1

	def test_fstroka(self):
		assert fstroka(1, 2, "1+1+1") == "2+1"

	def test_fz(self):
		assert fz("1111") == 1

if __name__ == '__main__':
	unittest.main()
