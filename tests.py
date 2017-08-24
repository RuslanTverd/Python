import unittest
from main.kalkulator import addition

class TestStringMethods(unittest.TestCase):
	def test_addition(self):
		assert addition(2,2) == 4

if __name__ == '__main__':
	unittest.main()

def addition(x,y):
    return x+y