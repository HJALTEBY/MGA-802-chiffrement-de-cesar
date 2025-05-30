"""
:file: unit_test_brute_force.py
:brief: Test unitaire pour la fonction brute force. Il suffit de lancer le fichier pour tester toutes les fonctions!
"""

import unittest
from cryptographie.recherche_mot import brute_force_methode_1

# Messages utilisés pour les tests. Comme nous le faisons à la main, nous testons seulement des clés avec un décalage de 1.
chemin_fichier_mots = "../data/dict-fr-AU-DELA-common-words.ascii"
message_base = "abeille"
message_base_cle_17 = "" #Trouvé avec notre propre fonction d'encryptage une fois les test unitaires effectués


class MyTestCase(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(brute_force_methode_1("abeille",chemin_fichier_mots), ("abeille",0))
        self.assertEqual(brute_force_methode_1("rsvzccv", chemin_fichier_mots), ("abeille", 17))
        # L'encryptage retire les accents et passe tout en minuscule.


if __name__ == '__main__':
    unittest.main()
