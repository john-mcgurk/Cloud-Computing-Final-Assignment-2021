import unittest
import multiplynum

class TestMultiplyNumber(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiplynum.multiply(2,4),8)
        self.assertEqual(multiplynum.multiply(2,1),2)
        self.assertEqual(multiplynum.multiply(8,0),0)

if __name__ == '__main__':
    unittest.main()
