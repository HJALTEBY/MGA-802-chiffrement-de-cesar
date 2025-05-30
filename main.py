from model import *
from brute_force import *
from gestion_character import retirer_accents

while True:
    obj = retirer_accents(input('Voulez-vous encrypter ou décrypter ? ').lower())
    if obj == 'encrypter':
        print('fonction encrypter')
        break
    elif obj == 'decrypter':
        message_a_decrypter = retirer_accents(input('Entrez le message à décrypter:')).lower()
        while True:
            liste_reponse = ['yes', 'oui', 'non', 'no']
            cb = retirer_accents(input('Connaissez-vous la combinaison ? ')).lower()
            if cb not in liste_reponse:
                print('Réponse non-valide')
            elif cb == 'no' or cb == 'non':
                print('brute_force')
                brute_force(message_a_decrypter,"data/dict-fr-AU-DELA-common-words.ascii")
                break
            else:  # la reponse est oui ou yes
                print(f'Je connais la combinaison')
                print('fonction_decrypter')
def encryptage_terminal():
    """
    Procédure demandant à l'utilisateur un message qu'il souhaite encoder et affiche l'encodage du message.
    :return:
    """
    # Les fonctions d'encryptage et de decalage propagent des exceptions. C'est ici qu'elles sont gérées.
    while True:
        message_a_encrypter = retirer_accents(input('Entrez le message à encrypter:').lower())
        cle = input('Entrez une clé de cryptage entre 0 et 25:')

        try:
            encrypter(message_a_encrypter, cle)
        except TypeError as e:
            # Si message_a_encrypter n'a pas le bon type ou si la cle entrée n'est pas un format valide, on
            # affiche l'exception et on redemande à l'utilisateur de rentrer une valeur valide.'
            print(e)

        # Si aucune exception n'est levée, on peut continuer!
        else:
            break
    return

def decryptage_terminal():
    """
    Procédure demandant à l'utilisateur un message qu'il souhaite decoder ainsi que la clé de décodage du message.
    :return:
    """
    # Les fonctions d'encryptage et de decalage propagent des exceptions. C'est ici qu'elles sont gérées.
    while True:
        message_a_decrypter = retirer_accents(input('Entrez le message à décrypter:').lower())
        cle = input('Entrez une clé de cryptage entre 0 et 25:')

        try:
            decrypter(message_a_decrypter, cle)
        except TypeError as e:
            # Si message_a_encrypter n'a pas le bon type ou si la cle entrée n'est pas un format valide, on
            # affiche l'exception et on redemande à l'utilisateur de rentrer une valeur valide.'
            print(e)

        # Si aucune exception n'est levée, on peut continuer!
        else:
            break
    return

def decryptage_fichier():
    """
    Procédure demandant à l'utilisateur un fichier contenant un message qu'il souhaite decoder ainsi que la clé de
    décodage du message.
    :return:
    """
    # Les fonctions d'encryptage et de decalage propagent des exceptions. C'est ici qu'elles sont gérées.


    compteur = 0
    while True:
        fichier_a_decrypter = retirer_accents(input('Entrez le fichier à décrypter:').lower())
        cle = input('Entrez une clé de cryptage entre 0 et 25:')

        try:
            decrypter_fichier(fichier_a_decrypter, cle)
        except TypeError as e:
            # Si message_a_encrypter n'a pas le bon type ou si la cle entrée n'est pas un format valide, on
            # affiche l'exception et on redemande à l'utilisateur de rentrer une valeur valide.'
            print(e)

        # L'exception est cette fois-ci due à une erreur de fichier inexistant.
        except FileNotFoundError as e:
            compteur += 1
            print("Votre fichier semble ne pas exister!")

            # Si l'utilisateur entre trop de fois un nom de fichier erroné, on le sort de la boucle.
            if compteur > 3:
                print("Limite atteinte pour la saisie du fichier.")
                break

        # Si aucune exception n'est levée, on peut continuer!
        else:
            break
    return

def choix_cle_ou_brute_force_message():
    """
    Demande à l'utilisateur de choisir entre la méthode brute force ou s'il connaît la clé dans le cas d'un décryptage
    d'un message via le terminal.
    :return:
    """
    while True:
        liste_reponse = ['yes', 'oui', 'non', 'no']
        cb = retirer_accents(input('Connaissez-vous la combinaison ? ')).lower()
        if cb not in liste_reponse:
            print('Réponse non-valide')
        elif cb == 'no' or cb == 'non':
            # brute_force(mot_a_decrypter,"data/dict-fr-AU-DELA-common-words.ascii")
            print('brute_force via terminal')
            break
        else:  # la reponse est oui ou yes
            decryptage_terminal()
            break
    return

def choix_cle_ou_brute_force_fichier():
    """
    Demande à l'utilisateur de choisir entre la méthode brute force ou s'il connaît la clé dans le cas d'un décryptage
    d'un fichier.
    :return:
    """
    while True:
        liste_reponse = ['yes', 'oui', 'non', 'no']
        cb = retirer_accents(input('Connaissez-vous la combinaison ? ')).lower()
        if cb not in liste_reponse:
            print('Réponse non-valide')
        elif cb == 'no' or cb == 'non':
            # brute_force(mot_a_decrypter,"data/dict-fr-AU-DELA-common-words.ascii")
            print('brute_force via fichier')
            break
        else:  # la reponse est oui ou yes
            decryptage_fichier()
            break
    return

# Boucle principale de l'algorithme
while True:
    obj = retirer_accents(input('Voulez-vous encrypter ou décrypter ? ').lower())

    # encryptage d'un message
    if obj == 'encrypter':
        # On choisi entre encrypter un fichier ou un message.
        encryptage_terminal()
        break

    # décryptage d'un message'
    elif obj == 'decrypter':
        #mot_a_decrypter = retirer_accents(input('Entrez le mot à décrypter:')).lower()
        while True:
            reponse = retirer_accents(input('Souhaitez-vous décrypter un message ou un fichier? (message/fichier)')).lower()
            if reponse == 'fichier':
                choix_cle_ou_brute_force_fichier()
                break
        break
    else:
        print('La réponse est non valide')

"""
TODO:  Mettre des commentaires et expliquer ce que fait le script en commentaire au début du fichier
"""