
#Unit test for fizzbuzz program 
import unittest 
import fizzbuzz


class testCase(unittest.TestCase):
    #def setup(self):
        #self.fizzbuzz = fizzbuzz()
    #Test 1 will pass 
    def test1(self):
        self.assertEqual(fizzbuzz, 'Fizz')

if __name__ == "__main__":
    unittest.main()

