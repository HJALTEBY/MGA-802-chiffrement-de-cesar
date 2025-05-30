from gestion_character import *
from cryptographie.encryption_decryption import *
from cryptographie.recherche_mot import *

def encryptage_terminal():
    """
    Procédure demandant à l'utilisateur un message qu'il souhaite encoder et affiche l'encodage du message.
    :return: None
    """
    # Les fonctions d'encryptage et de décalage propagent des exceptions. C'est ici qu'elles sont gérées.
    while True:
        # On enlève les accents et on met en minuscules pour uniformiser l'entrée utilisateur
        message_a_encrypter = retirer_accents(input('Entrez le message à encrypter:').lower())
        cle = input('Entrez une clé de cryptage entre 0 et 25:')

        try:
            # Tentative d'encryptage avec la clé fournie
            encrypter(message_a_encrypter, cle)
        except TypeError as e:
            # Si le type de données n'est pas correct ou la clé est invalide, on affiche l'erreur
            print(e)
        else:
            # Si l'encryptage se passe bien, on sort de la boucle
            break
    return


def decryptage_terminal(message):
    """
    Procédure demandant à l'utilisateur la clé de décryptage d’un message.
    :param message: le message chiffré à décrypter
    :return: None
    """
    # Même structure que l'encryptage : gestion des exceptions pour des saisies incorrectes
    while True:
        cle = input('Entrez une clé de cryptage entre 0 et 25:')

        try:
            decrypter(message, cle)
        except TypeError as e:
            # Erreur de type ou clé invalide
            print(e)
        else:
            break
    return


def ouvrir_nom_fichier():
    """
    Demande à l'utilisateur le nom d’un fichier à lire.
    Tente d’ouvrir ce fichier jusqu’à 3 fois en cas d’erreur.
    :return: le texte lu ou None si 3 erreurs consécutives
    """
    compteur = 0
    while True:
        try:
            fichier = input('Veuillez entrer le nom du fichier à lire (.txt) : ')
            f = open(fichier, 'r')  # Ouverture du fichier en lecture
            txt = f.read()
            print(txt)  # Affiche le contenu du fichier
        except FileNotFoundError as e:
            compteur += 1
            print("Votre fichier semble ne pas exister!")

            # Limite de tentatives atteinte
            if compteur > 3:
                return None
                break
        return txt


def choix_cle_ou_brute_force(mot_a_decrypter):
    """
    Propose à l'utilisateur de décrypter un message avec une clé connue ou via la méthode brute force.
    :param mot_a_decrypter: Le message à décrypter
    :return: la clé trouvée ou None si non trouvée
    """
    cle_decryptage = None
    while cle_decryptage is None:
        liste_reponse = ['yes', 'oui', 'non', 'no']
        cb = retirer_accents(input('Connaissez-vous la combinaison ? ')).lower()

        if cb not in liste_reponse:
            print('Réponse non-valide')

        elif cb == 'no' or cb == 'non':
            # Méthode automatique ou manuelle de brute force
            numero_methode = input('Voulez-vous utiliser la méthode automatique (1) ou manuel (2) ? : ')
            if numero_methode == '1':
                print('brute_force automatique via terminal')
                cle_decryptage = brute_force(mot_a_decrypter, "data/dict-fr-AU-DELA-common-words.ascii")
                break
            elif numero_methode == '2':
                print('brute_force manuel via terminal')
                cle_decryptage = brute_force_methode_2(mot_a_decrypter)
        else:  # si réponse = oui ou yes, alors demande la clé et déchiffre
            decryptage_terminal(mot_a_decrypter)
            break
    return cle_decryptage


# Boucle principale de l'algorithme
while True:
    obj = retirer_accents(input('Voulez-vous encrypter ou décrypter ? ').lower())

    # encryptage d'un message
    if obj == 'encrypter':
        # Choix d'encrypter un message (l'encryptage de fichier n’est pas proposé ici)
        encryptage_terminal()
        break

    elif obj == 'decrypter':
        # L’utilisateur décide de décrypter un message ou un fichier
        while True:
            reponse = retirer_accents(input('Souhaitez-vous décrypter un message ou un fichier? (message/fichier)')).lower()

            if reponse == 'fichier':
                text = ouvrir_nom_fichier()
                if text is None:
                    print("Limite atteinte pour la saisie du fichier.")
                    break
                else:
                    choix_cle_ou_brute_force(text)
                break

            elif reponse == 'message':
                message_a_decrypter = retirer_accents(input('Quel message voulez-vous décrypter ? :'))
                cle = choix_cle_ou_brute_force(message_a_decrypter)
                print(f"La clé du code César est {cle}!")
                print("Voici le message décrypté : ")
                print(decrypter(message_a_decrypter, cle))
                break

        break  # Sortie de la boucle principale après traitement
    else:
        print('La réponse est non valide')
