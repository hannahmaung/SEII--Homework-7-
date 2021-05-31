#Unit test for leap year program 
import unittest 
from leapyear import test # type: ignore


class testCase(unittest.TestCase):

    #Test 1 will pass, 2012 is a leap year
    def test1(self):
        for input in [2012]:
            assert test(input) == True
    # Test 2 will pass, 2000 is a leap year
    def test2(self):
        for input in [2000]:
            assert test(input) == True
    # Test 2 will pass, 2001 is not a leap year
    def test3(self):
        for input in [2001]:
            assert test(input) == False

if __name__ == "__main__":
        unittest.main()

