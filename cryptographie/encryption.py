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
        raise TypeError

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
def decrypter(cleCryptage):
    fichierCrypte = int(str(input('Entrez le nom du fichier a decrypter (ne pas oublier le .txt): ')))
    with open(fichierCrypte, 'r', encoding = 'utf-8') as fio :
        # Lire le contenu du fichier
        contenuCrypte = fio.read()

    alphabetCrypte = decalage(cleCryptage)  # créer nouvel alphabet avec clé de cryptage
    contenuDecrypte = ''

    for l in contenuCrypte :
        contenuDecrypte[l] = alphabet[alphabetCrypte.find(l)]
    print(f'Voici le message crypte : {contenuDecrypte}')

