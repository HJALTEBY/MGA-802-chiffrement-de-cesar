import unicodedata
import re

def retirer_accents(input_str):
    """
    Supprime les accents d'une chaîne de character.
    :param input_str: Chaîne de caractère dont on veut retirer les accents.
    :return: La chaîne de character sans accents.
    """

    # Replace all special character by their compatible equivalent
    nfkd_form = unicodedata.normalize('NFKD', input_str)

    # Create a new str '' and append each character from the normalized form
    res = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    return res

def split_string(input_str):
    """
    Sépare une chaine de character en un tuple contenant les mots, les lettres, les espaces, les retours à la lignes et
    les ponctuations de manière séparées. Malheureusement elle ne permet pas de séparer les apostrophes.
    :param input_str: La chaine de character à traiter
    :return: Une liste avec les différents mots, espaces et ponctuations.
    :raise: TypeError si l'argument n'est pas une chaine de character.
    """

    if type(input_str) is not str:
        raise TypeError

    # Source: https://www.geeksforgeeks.org/python-string-split-including-spaces/
    # Source: https://www.w3schools.com/python/python_regex.asp
    return re.split(r"(\s+)",input_str)
