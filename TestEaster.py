import unittest
# import the code you want to test here
from easter import *

class TestNothing(unittest.TestCase):

    # The setUp() method is run before every test
    def setUp(self) -> None:
        self.dates: list[date] = [date(1982, 4, 11), date(1983, 4, 3),
                             date(1984, 4, 22), date(1985, 4, 7),
                             date(1986, 3, 30), date(1987, 4, 19),
                             date(1988, 4, 3), date(1989, 3, 26),
                             date(1990, 4, 15), date(1991, 3, 31),
                             date(1992, 4, 19), date(1993, 4, 11),
                             date(1994, 4, 3), date(1995, 4, 16),
                             date(1996, 4, 7), date(1997, 3, 30),
                             date(1998, 4, 12), date(1999, 4, 4),
                             date(2000, 4, 23), date(2001, 4, 15),
                             date(2002, 3, 31), date(2003, 4, 20),
                             date(2004, 4, 11), date(2005, 3, 27),
                             date(2006, 4, 16), date(2007, 4, 8),
                             date(2008, 3, 23), date(2009, 4, 12),
                             date(2010, 4, 4), date(2011, 4, 24),
                             date(2012, 4, 8), date(2013, 3, 31),
                             date(2014, 4, 20), date(2015, 4, 5),
                             date(2016, 3, 27), date(2017, 4, 16),
                             date(2018, 4, 1), date(2019, 4, 21),
                             date(2020, 4, 12), date(2021, 4, 4),
                             date(2022, 4, 17), date(2023, 4, 9),
                             date(2024, 3, 31), date(2025, 4, 20),
                             date(2026, 4, 5), date(2027, 3, 28),
                             date(2028, 4, 16), date(2029, 4, 1),
                             date(2030, 4, 21), date(2031, 4, 13),
                             date(2032, 3, 28), date(2033, 4, 17),
                             date(2034, 4, 9), date(2035, 3, 25),
                             date(2036, 4, 13), date(2037, 4, 5),
                             date(2038, 4, 25), date(2039, 4, 10),
                             date(2040, 4, 1), date(2041, 4, 21),
                             date(2042, 4, 6), date(2043, 3, 29),
                             date(2044, 4, 17), date(2045, 4, 9),
                             date(2046, 3, 25), date(2047, 4, 14),
                             date(2048, 4, 5)]


    # Every method that starts with the string "test"
    # will be executed as a unit test
    def test2024(self) -> None:
        self.assertEqual(self.dates[2024-1982], easter(2024))

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

    def testValid(self) -> None:
        for year in range(1982, 2049):
            with self.subTest(year = year):
                self.assertEqual(easter(year), self.dates[year-1982])

if __name__ == '__main__':
    unittest.main()

