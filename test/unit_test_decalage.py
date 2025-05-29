"""
@file unit_test_decalage.py
@brief Test unitaire pour la fonction decalage.
"""

import unittest
import gestion_character.decalage as dec

alphabet_decale_2 = 'cdefghijklmnopqrstuvwxyzab'
alphabet_decale_15 = 'pqrstuvwxyzabcdefghijklmno'
alphabet_decale_moin_11 = alphabet_decale_15
alphabet_decale_moin_1 = 'zabcdefghijklmnopqrstuvwxy'
alphabet_decale_0 = 'abcdefghijklmnopqrstuvwxyz'
alphabet_decale_26 = 'abcdefghijklmnopqrstuvwxyz'
alphabet_decale_25 = alphabet_decale_moin_1

# Test unitaire prouvant que la fonction decalage fonctionne correctement.

class MyTestCase(unittest.TestCase):
    def test_decalage(self):
        self.assertEqual(dec.decalage(0), alphabet_decale_0)
        self.assertEqual(dec.decalage(2), alphabet_decale_2)
        self.assertEqual(dec.decalage(15), alphabet_decale_15)
        self.assertEqual(dec.decalage(-11), alphabet_decale_moin_11)
        self.assertEqual(dec.decalage(-1), alphabet_decale_moin_1)
        self.assertEqual(dec.decalage(0), alphabet_decale_0)
        self.assertEqual(dec.decalage(26), alphabet_decale_26)
        self.assertEqual(dec.decalage(25), alphabet_decale_25)

        # On vérifie que la fonction ne fonctionne pas avec des types invalides.
        self.assertRaises(TypeError, dec.decalage, "a")
        self.assertRaises(TypeError, dec.decalage, None)
        # Bon là il faut vraiment vouloir embêter le programme pour en arriver là
        self.assertRaises(TypeError, dec.decalage, complex(0))

        # On vérifie que le cast s'effectue correctement si la clé n'est pas un entier mais peux être convertie.
        self.assertEqual(dec.decalage(0.000), alphabet_decale_0)
        self.assertEqual(dec.decalage(0.05), alphabet_decale_0)


if __name__ == '__main__':
    unittest.main()


