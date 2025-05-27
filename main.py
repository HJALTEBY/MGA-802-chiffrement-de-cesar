import string

from model import decalage
from brute_force import *
from gestion_character import retirer_accents


alphabet = string.ascii_lowercase

#Demande à l'utilisateur d'entrer la clé de cryptage et ensuite le message à crypter.
def encrypter():
    cle_de_cryptage = input('Quelle clé de cryptage voulez-vous utiliser ? (entrez un chiffre entier):')
    alphabetCrypte = decalage(cle_de_cryptage) #créer nouvel alphabet avec clé de cryptage
    contenuACrypter = str(input('Que voulez-vous encrypter ? :'))
    contenuCrypte = '' #chaine de car contenant le message crypté

    #boucle sur chaque lettre du message non crypté
    #à chaque lettre du message ini on retourne son index dans l'alphabet classique
    #à chaque lettre du message ini on ajoute la lettre de l'alphabet crypté correspondant à l'index trouvé dans l'alphabet classique
    for l in contenuACrypter:
        contenuCrypte[l] = alphabetCrypte[alphabet.find(l)]
    print(f'Voici le message crypte : {contenuCrypte}')

#décrypter dans le cas où on connait la clé
def decrypter(cleCryptage):
    fichierCrypte = str(input('Entrez le nom du fichier a decrypter (ne pas oublier le .txt): '))
    with open(fichierCrypte, 'r', encoding = 'utf-8') as fio :
        # Lire le contenu du fichier
        contenuCrypte = fio.read()

    alphabetCrypte = decalage(cleCryptage)  # créer nouvel alphabet avec clé de cryptage
    contenuDecrypte = ''

    for l in contenuCrypte :
        contenuDecrypte[l] = alphabet[alphabetCrypte.find(l)]
    print(f'Voici le message crypte : {contenuDecrypte}')
import string

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
