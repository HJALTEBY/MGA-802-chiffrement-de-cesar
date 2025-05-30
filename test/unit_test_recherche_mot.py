"""
:file: unit_test_recherche_mot.py
:brief: Test unitaire pour la fonction recherche_mot. Il suffit de lancer le fichier pour tester toutes les fonctions!
"""
import unittest
from cryptographie.recherche_mot import est_un_mot

chemin_dictionnaire = "../data/dict-fr-AU-DELA-common-words.ascii"


# Test unitaire prouvant que la fonction est un mot fonctionne correctement. Je me suis appuyé sur le template proposé
# par PyCharm pour réussir à exécuter des tests

class MyTestCase(unittest.TestCase):
    def test_est_un_mot(self):
        self.assertEqual(est_un_mot('abeille',chemin_dictionnaire), True)
        self.assertEqual(est_un_mot('baouilze', chemin_dictionnaire), False)

if __name__ == '__main__':
    unittest.main()


