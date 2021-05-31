
#Unit test for fizzbuzz program 
import unittest 
from fizzbuzz import test # type: ignore

class testCase(unittest.TestCase):
    #Test 1 will pass, 5 is a multiple of 5, which prints out Buzz
    def test1(self):
        for input in [5]:
            assert test(input) == 'Buzz'
    #Test 2 will pass, 15 is a multiple of both 3 and 5 which prints out "FizzBuzz"
    def test2(self):
        for input in [15]:
            assert test(input) == "FizzBuzz"

if __name__ == "__main__":
        unittest.main()

