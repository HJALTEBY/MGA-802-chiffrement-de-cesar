"""
:file: unit_test_decryptage.py
:brief: Test unitaire pour la fonction decrypter. Il suffit de lancer le fichier pour tester toutes les fonctions!
"""

import unittest
from cryptographie.encryption_decryption import decrypter, decrypter_fichier
from gestion_character import retirer_accents

# Messages utilisés pour les tests. Comme nous le faisons à la main, nous testons seulement des clés avec un décalage de 1.
message_base = "abc"
mot_encrypte_cle_1 = "bcd"
mot_encrypte_cle_moins_1 = "zab"
message_complexe = "Ceci est un message complexe!"
message_complexe_cle_1 = "dfdj ftu vo nfttbhf dpnqmfyf!"
message_tres_complexe = "Ceci est un message super complexe! Il y a de la ponctuation et des chiffres: 115531. Ceci étaient les chiffres en questions."
message_tres_complexe_cle_1 = "dfdj ftu vo nfttbhf tvqfs dpnqmfyf! jm z b ef mb qpoduvbujpo fu eft dijggsft: 115531. dfdj fubjfou mft dijggsft fo rvftujpot."

fichier_encrpyte = "../data/fichier_encrypte"

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(decrypter("abc", 0), message_base)
        self.assertEqual(decrypter(mot_encrypte_cle_1,1), "abc")
        self.assertEqual(decrypter(mot_encrypte_cle_moins_1, -1), "abc")
        self.assertEqual(decrypter(message_complexe_cle_1, 1), retirer_accents(message_complexe).lower())
        self.assertEqual(decrypter(message_tres_complexe_cle_1, 1), retirer_accents(message_tres_complexe).lower())

        # L'encryptage retire les accents et passe tout en minuscule.
        self.assertEqual(decrypter(message_tres_complexe, 0), retirer_accents(message_tres_complexe).lower())

        # On vérifie qu'une mauvaise entrée de clé ou de message génère une exception
        # L'encryptage n'accepte que les clés qui peuvent être converties en entiers.
        self.assertRaises(TypeError, decrypter, message_base,"aa")
        self.assertRaises(TypeError, decrypter, message_base, [1,"a",2])

        # L'encryptage n'accepte qu'une chaine de caractère en entrée
        self.assertRaises(TypeError, decrypter, 123, [1, "a", 2])
        self.assertRaises(TypeError, decrypter, 123, 2)

        # Test pour la version faisant appel à un fichier
        self.assertEqual(decrypter_fichier(fichier_encrpyte, 1), retirer_accents(message_tres_complexe).lower())

        # Etant donné que la fonction fait directement appel à la fonction decrypter de base, on considère les tests du
        # dessus comme valides pour cette fonctions-ci

if __name__ == '__main__':
    unittest.main()
