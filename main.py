import string

# Fonction pour décaler les lettres de l'alphabet en fonction de la clé
def decalage(cle) :
    # on crée une chaine de caractère correspondant à l'alphabet
    alphabet = string.ascii_lowercase
    # on passe la chaine de caractère en liste :
    # https://www.ionos.fr/digitalguide/sites-internet/developpement-web/python-string-to-list/
    liste_alphabet = list(alphabet)
    # on cré une chaine de caractères vide
    alphabet_code = ""
    #Condition pour s'assurer que la clé est entre 26 et -26
    if cle > 26 or cle < -26 :
        new_cle = cle % 26
    else :
        new_cle = cle
    # condition si la clé est positive
    if new_cle > 0 :
        # boucle sur l'indice de liste_alphabet, où on démarre
        # à l'indice correspondant à la clé jusqu'à la fin de
        # l'alphabet
        for i in range(0+new_cle,26) :
            alphabet_code += liste_alphabet[i]
        # boucle sur l'indice de liste_alphabet, où on démarre
        # à l'indice 0 et on va jusqu'à l'indice correspond à
        # la clé
        for i in range(0,new_cle) :
            alphabet_code += liste_alphabet[i]
    # condition si la clé est négative
    elif new_cle < 0 :
        # boucle sur l'indice de liste_alphabet, où on démarre
        # à l'indice correspondant à celui de la fin moins la clé
        # jusqu'à la fin de l'alphabet
        for j in range((26+new_cle),26) :
            alphabet_code += liste_alphabet[j]
        # boucle sur l'indice de liste_alphabet, où on démarre
        # à l'indice 0 jusqu'à la fin de l'alphabet en enlevant
        # le nombre correspondant à la clé
        for j in range(0,(26+new_cle)) :
            alphabet_code += liste_alphabet[j]
    # la clé est nulle (pas de changement)
    else :
        alphabet_code = alphabet
    return alphabet_code

