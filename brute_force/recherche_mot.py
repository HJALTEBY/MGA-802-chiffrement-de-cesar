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

def brute_force(mot_a_decoder,fichier):
    """
    Change la clé du code César jusqu'à tomber sur un mot valide.
    :param mot_a_trouver: La chaîne de character que l'on souhaite décoder.
    :param fichier: Le fichier contenant la liste de mots valide.
    :return: None si aucune clé n'est trouvée. Retourne la valeur de la clé si une clé a été trouvée.
    """

    cle = 0
    # On vérifie si la str est un mot. Si ce n'est pas le cas, on recommence en incrémentant la clé de 1.
    while not est_un_mot(mot_a_decoder,fichier) and cle <= 26:
        print("Ce n'est pas la bonne clé")
        print("Décodage avec la clé suivante")
        cle += 1

    # On a pas trouvé la clé :(
    if cle < 26:
        print("Aucune clé n'a été trouvée :(")

    #On a trouvé la clé
    else:
        print(f"la clé du code César est {cle}!")
