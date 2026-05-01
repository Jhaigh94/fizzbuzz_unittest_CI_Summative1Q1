import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_no1(self):
        self.assertEqual(fizzbuzz(1),"1")

    def test_multiple3(self):
        self.assertEqual(fizzbuzz(3),"Fizz")
    
    def test_multiple5(self):
        self.assertEqual(fizzbuzz(5),"Buzz")   

if __name__ == "__main__":
    unittest.main()