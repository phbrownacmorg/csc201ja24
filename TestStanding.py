import unittest
# import the code you want to test here
import class_standing

class TestNothing(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test

    # Bottom of the freshman range
    def testZero(self) -> None:
        self.assertEqual(class_standing.standing(0), 'freshman')

    # Top of the freshman range
    def test23(self) -> None:
        self.assertEqual(class_standing.standing(23), 'freshman')

    # Bottom of the sophomore range
    def test24(self) -> None:
        self.assertEqual(class_standing.standing(24), 'sophomore')

    # Top of the sophomore range
    def test55(self) -> None:
        self.assertEqual(class_standing.standing(55), 'sophomore')

    # Bottom of the junior range
    def test56(self) -> None:
        self.assertEqual(class_standing.standing(56), 'junior')

    # Top of the junior range
    def test86(self) -> None:
        self.assertEqual(class_standing.standing(86), 'junior')

    # Bottom of the senior range
    def test87(self) -> None:
        self.assertEqual(class_standing.standing(87), 'senior')

    # Typical senior at (or near) graduation
    def test120(self) -> None:
        self.assertEqual(class_standing.standing(120), 'senior')

    # Not a ceiling, just a high number.  Senior
    #   standing doesn't have a ceiling.
    def test180(self) -> None:
        self.assertEqual(class_standing.standing(180), 'senior')

if __name__ == '__main__':
    unittest.main()

