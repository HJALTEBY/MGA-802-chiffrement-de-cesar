"""
:file: recherche_mot.py
:brief: Cherche si une chaîne de caractères est un mot en effectuant une recherche dans un fichier contenant un grand
nombre de mots existants. Le fichier utilisé provient du package : https://pypi.org/project/dict-fr-AU-DELA/
"""
from cryptographie import decrypter
import re

# Chemin vers le fichier contenant les mots du dictionnaire
chemin_fichier_mots = "../data/dict-fr-AU-DELA-common-words.ascii"


def est_un_mot(mot_a_trouver, fichier):
    """
    Vérifie si un mot est présent dans un fichier. Cette fonction ignore les majuscules et les accents.
    :param mot_a_trouver: Le mot à chercher.
    :param fichier: Le fichier dans lequel chercher le mot.
    :return: True si le mot est présent dans le fichier, False sinon.
    """

    # Ouverture du fichier et chargement de tout le contenu
    with open(fichier, 'r') as file:
        text = file.read()
        mots = text.split()  # On divise le contenu du fichier en mots (séparés par des espaces ou retours à la ligne)

    # On vérifie si le mot apparaît au moins une fois dans la liste des mots
    if mots.count(mot_a_trouver) != 0:
        return True
    else:
        return False


def est_un_mot_version_manu(mot_a_trouver):
    """
    Vérifie manuellement si une chaîne est un mot en demandant à l'utilisateur.
    :param mot_a_trouver: Le mot à vérifier.
    :return: True si l'utilisateur confirme que c'est un mot, False sinon.
    """

    # On boucle jusqu'à obtenir une réponse valide de l'utilisateur
    while True:
        # On convertit la réponse en minuscules pour simplifier la vérification
        reponse_utilisateur = input(f"La chaîne de caractères '{mot_a_trouver}' est-elle un mot ? (oui/non) ").lower()
        if reponse_utilisateur == 'oui':
            return True
        elif reponse_utilisateur == 'non':
            return False
        else:
            print(f"'{reponse_utilisateur}' n'est pas une réponse valide.")  # Message d'erreur en cas de saisie incorrecte


def brute_force(mess_a_decoder, fichier):
    """
    Tente de décrypter un message codé avec un code César en testant toutes les clés possibles (0 à 26).
    :param mess_a_decoder: La chaîne de caractères à décoder.
    :param fichier: Le fichier contenant les mots valides.
    :return: La clé trouvée si succès, None sinon.
    """
    cle = 0
    # On découpe le message en mots à l'aide de séparateurs usuels (ponctuation, espaces, tabulations, sauts de ligne)
    list_de_mot = re.split(r"[ ',.!?\t\n]", mess_a_decoder)
    print(list_de_mot)

    # On parcourt les mots trouvés
    for m in list_de_mot:
        if len(m) > 1:  # On ignore les lettres seules
            # On teste les différentes clés jusqu'à trouver un mot valide ou dépasser 26
            while not est_un_mot(decrypter(m, cle), fichier) and cle <= 26:
                print("<décodage en cours...> Ce n'est pas la bonne clé")
                cle += 1
                # Affiche la clé en cours de test
                print(f"<décodage en cours...> Décodage avec la clé suivante : cle = {cle}")

            if cle > 26:
                print("Aucune clé n'a été trouvée :(")  # Toutes les clés ont été testées sans succès
                return None
            else:
                # Clé trouvée ! On la retourne.
                return cle


def brute_force_methode_2(mess_a_decoder):
    """
    Variante manuelle de brute_force : l'utilisateur valide lui-même les mots potentiels.
    :param mess_a_decoder: La chaîne à décoder.
    :return: None si aucune clé trouvée, sinon retourne la clé trouvée.
    """
    mot_a_decoder = None
    # On découpe le message en mots avec les mêmes séparateurs que précédemment
    list_de_mot = re.split(r"[ ',.!?\t\n]", mess_a_decoder)

    # On récupère le premier mot de plus d'une lettre
    while mot_a_decoder is None:
        for m in list_de_mot:
            if len(m) > 1:
                mot_a_decoder = m
                break

    cle = 0

    # On teste chaque clé tant que le mot décrypté n'est pas reconnu comme valide par l'utilisateur
    while not est_un_mot_version_manu(decrypter(mot_a_decoder, cle)) and cle <= 26:
        #print(cle)
        #print("Ce n'est pas la bonne clé")
        cle += 1
        #print(f"Décodage avec la clé suivante : cle = {cle}")

    # Aucune clé valide n'a été trouvée
    if cle > 26:
        print("Aucune clé n'a été trouvée :(")
        return None

    else:
        # Une clé correcte a été trouvée
        return cle

