
#Unit test for fizzbuzz program 
import unittest 
from fizzbuzz import test # type: ignore

class testCase(unittest.TestCase):
    #Test 1 will pass 
    def test1(self):
        for input in [5]:
            assert test(input) == 'Buzz'

if __name__ == "__main__":
        unittest.main()

