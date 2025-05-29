import string

from model import encryption
from brute_force import *
from gestion_character import retirer_accents

# Boucle principale de l'algorithme
while True:
    obj = retirer_accents(input('Voulez-vous encrypter ou décrypter ? ').lower())

    # encryptage d'un message
    if obj == 'encrypter':
        encryption.encrypter()
        break

    # décryptage d'un message'
    elif obj == 'decrypter':
        mot_a_decrypter = retirer_accents(input('Entrez le mot à décrypter:')).lower()
        while True:
            liste_reponse = ['yes', 'oui', 'non', 'no']
            cb = retirer_accents(input('Connaissez-vous la combinaison ? ')).lower()
            if cb not in liste_reponse:
                print('Réponse non-valide')
            elif cb == 'no' or cb == 'non':
                brute_force(mot_a_decrypter,"data/dict-fr-AU-DELA-common-words.ascii")
                print('boute_force')
                break
            else:  # la reponse est oui ou yes
                print(f'Je connais la combinaison')
                print('fonction_decrypter')
                break
        break

    # réponse non valide
    else:
        print('La réponse est non valide')
        continue
