#Unit test for leap year program 
import unittest 
from leapyear import test # type: ignore

class testCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.test())

if __name__ == "__main__":
        unittest.main()

