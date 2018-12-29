#import unittest
import unittest

#define or import the function to be tested.
def multiply(a, b):
    return (a * b)

#create the test class.
class MultiplyTestCase(unittest.TestCase):

    #define your test method
    def test_multiply(self):
        product = multiply(3, 4)

        #check for your result
        self.assertEqual(12, product)

    def test_multiples_with_one_value_negative(self):
        product = multiply(-3, 4)
        self.assertEqual(-12, product)

    @unittest.skip("running the other two first to avoid test conflict.")
    def test_multiples_with_both_values_negative(self):
        product = multiply(-3, -4)
        self.assertEqual(12, product)

#make the scsript executable
if __name__=='__main__':
    unittest.main()
