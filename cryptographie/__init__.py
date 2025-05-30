from .encryption_decryption import *
from .recherche_mot import *


def help():
    """
    Affiche l'aide pour l'utilisation des fonctions du package.
    """
    print(encryption_decryption.__doc__)
    print(recherche_mot.__doc__)