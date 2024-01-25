import contextlib
import io
import unittest
# import the code you want to test here
from futureval import *

class TestFutureval(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def test_800_1_1(self) -> None:
        self.assertAlmostEqual(calc_futureval(800, 0.01, 1)[-1],
                                800.0 * 1.01 ** 1)

    def test_800_1_2(self) -> None:
        self.assertAlmostEqual(calc_futureval(800, 0.01, 2)[-1],
                                800 * 1.01 ** 2)

    def test_800_1_10(self) -> None:
        self.assertAlmostEqual(calc_futureval(800, 0.01, 10)[-1],
                                800 * 1.01 ** 10)

    def test_1000_5_10(self) -> None:
        self.assertAlmostEqual(calc_futureval(1000, .1333, 10)[-1],
                                1000 * 1.1333 ** 10)

    # Other tests of calc_futureval would likely be wanted
    
    def test_table_800_1_1(self) -> None:
        outstr = io.StringIO()
        with contextlib.redirect_stdout(outstr):
            print_table([800.0, 808.0])
        self.assertEqual(outstr.getvalue(),
                         """Period \t Interest \t   Amount   
Initial\t          \t$     800.00
   1\t$     8.00\t$     808.00\n""")

    def test_table_1000_1_2(self) -> None:
        outstr = io.StringIO()
        with contextlib.redirect_stdout(outstr):
            print_table([1000.0, 1010.0, 1020.1])
        self.assertEqual(outstr.getvalue(),
                         """Period \t Interest \t   Amount   
Initial\t          \t$    1000.00
   1\t$    10.00\t$    1010.00
   2\t$    10.10\t$    1020.10\n""")


if __name__ == '__main__':
    unittest.main()

