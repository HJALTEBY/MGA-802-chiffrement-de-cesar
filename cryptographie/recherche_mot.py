"""
:file: recherche_mot.py
:brief: Cherche si une chaîne de character est un mot est effectuant une recherche dans un fichier contenant un grand
nombre de mots existants. Le fichier utilisé provient du package: https://pypi.org/project/dict-fr-AU-DELA/
"""
from cryptographie import decrypter

chemin_fichier_mots = "../data/dict-fr-AU-DELA-common-words.ascii"

def est_un_mot(mot_a_trouver,fichier):
    """
    Cherche si un mot est présent dans uun fichier. Cette fonction ignore les majuscules et les accents.
    :param mot: Le mot à chercher.
    :param fichier: Le fichier dans lequel chercher le mot.
    :return: True si le mot est présent dans le fichier. False sinon.
    """

    #Ouverture du fichier et chargements des mots du dictionnaire
    with open(fichier, 'r') as file:
        text = file.read()
        mots = text.split()

    if mots.count(mot_a_trouver) != 0:
        return True
    else:
        return False

def est_un_mot_version_lente(mot_a_trouver):
    """
    Demande à l'utilisateur si le mot en question est un mot réel.
    :param mot_a_trouver: Le mot à vérifier
    :return: True si l'utilisateur considère que c'est un mot. False sinon.
    """

    # On ne sort pas de la boucle tant que l'on a pas eu une réponse de l'utilisateur.
    while True:
        # lower case pour permettre une meilleure prise en compte des réponses
        reponse_utilisateur = input(f"La chaine de character '{mot_a_trouver}' est-elle un mot? (oui/non) ").lower()
        if reponse_utilisateur == 'oui':
            return True
        elif reponse_utilisateur == 'non':
            return False
        else:
            print(f"'{reponse_utilisateur}' n'est pas une réponse valide.")


def brute_force(mess_a_decoder,fichier):
    """
    Change la clé du code César jusqu'à tomber sur un mot valide.
    :param mot_a_trouver: La chaîne de character que l'on souhaite décoder.
    :param fichier: Le fichier contenant la liste de mots valide.
    :return: None si aucune clé n'est trouvée. Retourne la valeur de la clé si une clé a été trouvée.
    """
    cle = 0
    list_de_mot = mess_a_decoder.split()


    # On vérifie si la str est un mot. Si ce n'est pas le cas, on recommence en incrémentant la clé de 1.
    #Si une clé unique pour tout le message, il suffit de vérifier le premier mot de la phrase cryptée
    #cette methode ne fonctionne qu'en partant du principe qu'une clé unique a été utilisé
    while not est_un_mot(decrypter(list_de_mot[0], cle), fichier) and cle <= 26:
        print("Ce n'est pas la bonne clé")
        cle += 1
        print("Décodage avec la clé suivante") #Mettre la fonction permettant de décoder le mot avec la clé n


    # On a pas trouvé la clé :(
    if cle > 26:
        print("Aucune clé n'a été trouvée :(")

    #On a trouvé la clé
    else:
        print(f"la clé du code César est {cle}! La phrase décrypté est la suivante :\n {decrypter(mess_a_decoder, cle)}")
        
