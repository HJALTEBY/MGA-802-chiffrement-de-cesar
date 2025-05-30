"""
:brief: méthodes permettant de décrypter et d'encrypter des messages contenus dans des chaînes de caractères.
"""
from gestion_character import retirer_accents
from gestion_character.decalage import decalage
import string

alphabet = string.ascii_lowercase

def encrypter(message,cle_de_cryptage):
    """
    Fonction permettant d'encrypter un message à partir d'une clé fournie et d'un message. La fonction se débarasse des
    accents du message et met le message en minuscule.
    :param: Une chaine de caractère à encrypter
    :param: Une clé de cryptage
    :return: La chaîne de caractère encryptée
    :raise: TypeError Si la clé entrée par l'utilisateur ne peut pas être considérée comme un entier ou si str n'est pas
    une chaîne de caractère.
    """

    alphabet_crypte = decalage(cle_de_cryptage) #créer nouvel alphabet avec clé de cryptage

    # Si l'entrée n'est pas une chaîne de caractère, on ne peut pas encrypter le message.
    if type(message) is not str:
        raise TypeError('Veuillez entrer une chaîne de caractère valide!')

    #On retire les accents du message et on met le message en minuscule
    message = retirer_accents(message).lower()
    contenu_crypte = '' #chaine de car contenant le message crypté

    #boucle sur chaque lettre du message non crypté
    #à chaque lettre du message ini on retourne son index dans l'alphabet classique
    #à chaque lettre du message ini on ajoute la lettre de l'alphabet crypté correspondant à l'index trouvé dans l'alphabet classique
    for l in message:
        # Si l n'est pas une lettre, source: https://sqlpey.com/python/top-7-methods-to-determine-if-character-in-python-string-is-a-letter/
        if l.isalpha():
            contenu_crypte += alphabet_crypte[alphabet.find(l)]
        else :
            contenu_crypte += l
    print(f'Voici le message crypte : {contenu_crypte}')
    return contenu_crypte

#décrypter dans le cas où on connait la clé
def decrypter(message, cleCryptage):
    """
    Fonction permettant de décrypter un message à partir d'une clé fournie et d'un message. La fonction retourne un message
    sans accents ni majuscules.
    :param: Une chaine de caractère à décrypter
    :param: Une clé de cryptage
    :return: La chaîne de caractère décryptée
    :raise: TypeError Si la clé entrée par l'utilisateur ne peut pas être considérée comme un entier ou si str n'est pas
    une chaîne de caractère.
    """

    # Si l'entrée n'est pas une chaîne de caractère, on ne peut pas encrypter le message.
    if type(message) is not str:
        raise TypeError('Veuillez entrer une chaîne de caractère valide!')

    # Retrait des accents et mise en minuscule
    message = retirer_accents(message).lower()

    alphabet_crypte = decalage(cleCryptage)  # créer nouvel alphabet avec clé de cryptage
    contenu_decrypte = ''

    for l in message :
        if l.isalpha():
            contenu_decrypte += alphabet[alphabet_crypte.find(l)]
        else :
            contenu_decrypte += l
    print(f'Voici le message decrypte : {contenu_decrypte}')

    #list_contenu_decrypte = contenu_decrypte.split()

    return contenu_decrypte

def decrypter_fichier(file, cle_cryptage):
    """
    Fonction permettant de décrypter un message contenu dans un fichier à partir d'une clé fournie. La fonction retourne
    un message sans accents ni majuscules.
    :param: Le chemin vers le fichier contenant le message à décrypter
    :param: Une clé de cryptage
    :return: La chaîne de caractère décryptée
    :raise: TypeError Si la clé entrée par l'utilisateur ne peut pas être considérée comme un entier ou si str n'est pas
    une chaîne de caractère.
    :raise: FileNotFoundError si le chemin vers le fichier n'existe pas.
    """

    with open(file, 'r', encoding='utf-8') as fio:
        # Lire le contenu du fichier
        contenu_crypte = fio.read()

    return decrypter(contenu_crypte,cle_cryptage)
