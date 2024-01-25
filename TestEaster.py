import unittest
# import the code you want to test here
from easter import *

class TestNothing(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def test2024(self) -> None:
        self.assertEqual(date(2024, 3, 31), easter(2024))

    def test1981(self) -> None:
        with self.assertRaises(ValueError) as cm:
            easter(1981)
        xc: ValueError = cm.exception
        self.assertEqual(xc.args[0], 
                         'Year must be in the range 1982-2048, inclusive.')

    def test2049(self) -> None:
        with self.assertRaises(ValueError) as cm:
            easter(2049)
        xc: ValueError = cm.exception
        self.assertEqual(xc.args[0], 
                         'Year must be in the range 1982-2048, inclusive.')



if __name__ == '__main__':
    unittest.main()

