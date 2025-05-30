from .encryption import *
from .recherche_mot import *

def help():
    """
    Affiche l'aide pour l'utilisation des fonctions du package.
    """
    print(encryption.__doc__)
    print(recherche_mot.__doc__)