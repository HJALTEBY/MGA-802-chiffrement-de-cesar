import unicodedata

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