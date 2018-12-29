#Testing the method add
import unittest

#define / import function to be tested
def add(x, y):
    return (x + y)

#create a testcase class
class AddTestCase(unittest.TestCase):

    #create your test method
    def test_add(self):
        sum = add(4, 5)

        #test the method
        self.assertEqual(9, sum)

#make the script executable
if __name__=='__main__':
    unittest.main()
