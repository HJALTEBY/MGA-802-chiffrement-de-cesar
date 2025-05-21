from brute_force import *
import unittest

chemin_dictionnaire = "../data/dict-fr-AU-DELA-common-words.ascii"

class MyTestCase(unittest.TestCase):
    def test_est_un_mot(self):
        self.assertEqual(est_un_mot('abeille',chemin_dictionnaire), True)
        self.assertEqual(est_un_mot('baouilze', chemin_dictionnaire), False)

if __name__ == '__main__':
    unittest.main()


