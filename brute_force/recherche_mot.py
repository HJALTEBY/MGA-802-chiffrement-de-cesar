chemin_dictionnaire = "../data/dict-fr-AU-DELA-common-words.ascii"

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

print(est_un_mot('abeille',chemin_dictionnaire))