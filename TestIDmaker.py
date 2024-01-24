import unittest
# import the code you want to test here
from idmaker_files import *

class TestIDmaker(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testSimplifyBrown(self) -> None:
        self.assertEqual(simplify_name('Brown'), 'Brown')

    def testSimplifySpaces(self) -> None:
        self.assertEqual(simplify_name('von Richthofen'), 'vonRichthofen')

    def testSimplifyOBrien(self) -> None:
        self.assertEqual(simplify_name("O'Brien"), "OBrien")

    def testSimplifyHaden(self) -> None:
        self.assertEqual(simplify_name("Hådén"), "Haden")

    def testSimplifyHyphen(self) -> None:
        self.assertEqual(simplify_name("Harrison-Maguire"), "Harrison-Maguire")
    
    def testInitialsSimple(self) -> None:
        self.assertEqual(make_initials('Laura Feitzinger'), 'LF')

    def testInitialsInitial(self) -> None:
        self.assertEqual(make_initials('Peter H.'), 'PH')

    def testInitialsSingle(self) -> None:
        self.assertEqual(make_initials('Peter'), 'P')

    def testInitialsMultiple(self) -> None:
        self.assertEqual(make_initials('William Arthur Philip Louis'), 'WA')

    def testMakeUserIDs(self) -> None:
        self.assertEqual(make_userids([['Brown', 'Peter H.'],
                                       ['Brown', 'Laura Feitzinger'],
                                       ['von Richthofen', 
                                        'Manfred Albrecht'],
                                       ["O'Brian", "Brian Boru"],
                                       ["Hådén", 'Johannes E. A.'],
                                       ['Harrison-Maguire', 'Kelly'],
                                       ['Windsor', 
                                        'William Arthur Philip Louis']]),
        [['Brown', 'Peter H.', 'phbrown001'],
         ['Brown', 'Laura Feitzinger', 'lfbrown001'],
         ['von Richthofen', 'Manfred Albrecht', 'mavonrichthofen001'],
         ["O'Brian", "Brian Boru", 'bbobrian001'],
         ["Hådén", 'Johannes E. A.', 'jehaden001'],
         ['Harrison-Maguire', 'Kelly', 'kharrison-maguire001'],
         ['Windsor', 'William Arthur Philip Louis', 'wawindsor001']])

if __name__ == '__main__':
    unittest.main()

