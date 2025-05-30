"""
:file: unit_test_encryptage.py
:brief: Test unitaire pour la fonction encrypter. Il suffit de lancer le fichier pour tester toutes les fonctions!
"""

import unittest
from cryptographie.encryption_decryption import encrypter
from gestion_character import retirer_accents

# Messages utilisés pour les tests. Comme nous le faisons à la main, nous testons seulement des clés avec un décalage de 1.
message_base = "abc"
mot_encrypte_cle_1 = "bcd"
mot_encrypte_cle_moins_1 = "zab"
message_complexe = "Ceci est un message complexe!"
message_complexe_cle_1 = "dfdj ftu vo nfttbhf dpnqmfyf!"
message_tres_complexe = "Ceci est un message super complexe! Il y a de la ponctuation et des chiffres: 115531. Ceci étaient les chiffres en questions."
message_tres_complexe_cle_1 = "dfdj ftu vo nfttbhf tvqfs dpnqmfyf! jm z b ef mb qpoduvbujpo fu eft dijggsft: 115531. dfdj fubjfou mft dijggsft fo rvftujpot."

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(encrypter("abc", 0), message_base)
        self.assertEqual(encrypter("abc",1), mot_encrypte_cle_1)
        self.assertEqual(encrypter("abc", -1), mot_encrypte_cle_moins_1)
        self.assertEqual(encrypter(message_complexe, 1), message_complexe_cle_1)
        self.assertEqual(encrypter(message_tres_complexe, 1), message_tres_complexe_cle_1)

        # L'encryptage retire les accents et passe tout en minuscule.
        self.assertEqual(encrypter(message_tres_complexe, 0), retirer_accents(message_tres_complexe).lower())

        # On vérifie qu'une mauvaise entrée de clé ou de message génère une exception
        # L'encryptage n'accepte que les clés qui peuvent être converties en entiers.
        self.assertRaises(TypeError, encrypter, "abc","aa")
        self.assertRaises(TypeError, encrypter, "abc", [1,"a",2])

        # L'encryptage n'accepte qu'une chaine de caractère en entrée
        self.assertRaises(TypeError, encrypter, 123, [1, "a", 2])
        self.assertRaises(TypeError, encrypter, 123, 2)

if __name__ == '__main__':
    unittest.main()
