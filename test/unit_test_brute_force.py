"""
:file: unit_test_brute_force.py
:brief: Test unitaire pour la fonction brute force. Il suffit de lancer le fichier pour tester toutes les fonctions!
"""

import unittest
from unittest import mock
from cryptographie.recherche_mot import brute_force_methode_2

# Messages utilisés pour les tests. Comme nous le faisons à la main, nous testons seulement des clés avec un décalage de 1.
chemin_fichier_mots = "../data/dict-fr-AU-DELA-common-words.ascii"
message_base = "abeille"
message_base_cle_17 = "" #Trouvé avec notre propre fonction d'encryptage une fois les test unitaires effectués


class MyTestCase(unittest.TestCase):
    # La fonction ci dessous permet de faire du mocking, de simuler une entrée de l'utilisateur dans la console
    # Source: https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
    # Source 2: https://dnmtechs.com/mocking-user-input-for-unit-testing-in-python-3/
    @mock.patch('builtins.input', create=True)
    def test_brute_force_user_input(self, mocked_input):
        mocked_input.side_effect = ['oui']
        self.assertEqual(brute_force_methode_2("abeille"), ("abeille",0))

        # Cette fois-ci l'utilisateur va devoir dire non pour les clés 0 à 16 et dire oui pour la clé 17
        mocked_input.side_effect = ['non', 'non', 'non', 'non', 'non', 'non', 'non', 'non', 'non', 'non', 'non', 'non', 'non', 'non', 'non', 'non', 'non', 'oui']
        self.assertEqual(brute_force_methode_2("rsvzccv"), ("abeille", 17))


"""
    def test_brute_force(self):
        self.assertEqual(brute_force_methode_1("abeille",chemin_fichier_mots), ("abeille",0))
        self.assertEqual(brute_force_methode_1("rsvzccv", chemin_fichier_mots), ("abeille", 17))
        # L'encryptage retire les accents et passe tout en minuscule.
"""

if __name__ == '__main__':
    unittest.main()
