import unittest
# import the code you want to test here
from eligibility import *

class TestEligibility(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testHR_35_native(self) -> None:     # representative case (pun
        self.assertTrue(eligibleHR(35, 35)) # intended, I suppose)

    # Boundary case for citizenship (True)
    def testHR_35_7(self) -> None:
        self.assertTrue(eligibleHR(35, 7))

    # Boundary case for citizenship (False)
    def testHR_35_6(self) -> None:
        self.assertFalse(eligibleHR(35, 6))

    # Boundary case for age (True)
    def testHR_25_native(self) -> None:
        self.assertTrue(eligibleHR(25, 25))

    # Boundary case for age (False)
    def testHR_24_native(self) -> None:
        self.assertFalse(eligibleHR(24, 24))

    # Representative case for neither (False)
    def testHR_20_0(self) -> None:
        self.assertFalse(eligibleHR(20, 0))

    # Boundary case for both (False)
    def testHR_24_6(self) -> None:
        self.assertFalse(eligibleHR(24, 6))

    # Boundary case for both (True)
    def testHR_25_7(self) -> None:
        self.assertTrue(eligibleHR(25, 7))


if __name__ == '__main__':
    unittest.main()

