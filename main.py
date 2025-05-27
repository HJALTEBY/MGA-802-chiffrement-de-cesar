from model import *
from brute_force import *
from gestion_character import retirer_accents

while True:
    obj = retirer_accents(input('Voulez-vous encrypter ou décrypter ? ').lower())
    if obj == 'encrypter':
        print('fonction encrypter')
        break
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
    else:
        print('La réponse est non valide')

"""
TODO:  Mettre des commentaires et expliquer ce que fait le script en commentaire au début du fichier
"""