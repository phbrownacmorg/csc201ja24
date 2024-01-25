import unittest
# import the code you want to test here
from quadratic import *
import math

class TestQuadratic(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testRoots_1_0_0(self) -> None:
        self.assertAlmostEqual(find_roots(1, 0, 0)[0], 0)
        self.assertAlmostEqual(find_roots(1, 0, 0)[1], 0)

    def testRoots_1_3_2(self) -> None:
        self.assertAlmostEqual(find_roots(1, 3, 2)[0], -1)
        self.assertAlmostEqual(find_roots(1, 3, 2)[1], -2)

    def testRoots_1_n3_2(self) -> None:
        self.assertAlmostEqual(find_roots(1, -3, 2)[0], 2)
        self.assertAlmostEqual(find_roots(1, -3, 2)[1], 1)
    
    def testRoots_1_n3_n2(self) -> None:
        self.assertAlmostEqual(find_roots(1, -3, -2)[0], 
                               (3 + math.sqrt(17))/2)
        self.assertAlmostEqual(find_roots(1, -3, -2)[1], 
                               (3 - math.sqrt(17))/2)

    def testRoots_2_n5_2(self) -> None:
        self.assertAlmostEqual(find_roots(2, -5, 2)[0], 2)
        self.assertAlmostEqual(find_roots(2, -5, 2)[1], 0.5)

    def testRoots_1_2_3(self) -> None:
        with self.assertRaises(ValueError) as cm:
            find_roots(1, 2, 3)
        xc: ValueError = cm.exception
        self.assertEqual(xc.args[0], 'math domain error')

    def testRoot_1_3_2p5(self) -> None:
        with self.assertRaises(ValueError) as cm:
            find_roots(1, 3, 2.5)
        xc: ValueError = cm.exception
        self.assertEqual(xc.args[0], 'math domain error')

if __name__ == '__main__':
    unittest.main()

