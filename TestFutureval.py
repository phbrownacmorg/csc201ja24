import unittest
# import the code you want to test here
from futureval import *

class TestFutureval(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def test800_1_1(self) -> None:
        self.assertAlmostEqual(calc_futureval(800, 0.01, 1)[-1],
                                800.0 * 1.01 ** 1)

    def test800_1_2(self) -> None:
        self.assertAlmostEqual(calc_futureval(800, 0.01, 2)[-1],
                                800 * 1.01 ** 2)

    def test800_1_10(self) -> None:
        self.assertAlmostEqual(calc_futureval(800, 0.01, 10)[-1],
                                800 * 1.01 ** 10)

    def test1000_5_10(self) -> None:
        self.assertAlmostEqual(calc_futureval(1000, .1333, 10)[-1],
                                1000 * 1.1333 ** 10)

    # Other tests would be wanted

if __name__ == '__main__':
    unittest.main()

