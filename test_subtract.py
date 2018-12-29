#import unittest
import unittest

#define or import function to be tested
def subtract(a, b):
    return (a - b)

#create our test class
class SubtractTestCase(unittest.TestCase):

    #define test_method
    def test_subtract(self):
        difference = subtract(4, 1)
        #check for correctness of your result
        self.assertEqual(3, difference)

    def test_subtract_one_negative(self):
        difference = subtract(-4, 1)
        self.assertEqual(-5, difference)

    def test_subtract_both_negative(self):
        difference = subtract(-4, -1)
        self.assertEqual(-3, difference)

#make the script executable
if __name__ == '__main__':
    unittest.main()
