"""
Ce script permet de calculer l'efficacité des deux fonctions brute force créées
"""

from time import perf_counter
from cryptographie import brute_force
from cryptographie import brute_force_methode_2

# on demande le mot à décrypter à l'utilisateur
mot = str(input("Entrez le mot que vous souhaitez décrypter : "))
# on donne directement le nom du fichier avec la liste de mot
fichier = "../data/dict-fr-AU-DELA-common-words.ascii"


# Evaluation du temps d'exécution pour l'exemple
# Moyenne de ce temps pour un certain nombre de répétitions
# on demande le nombre de répétition que veut faire l'utilisateur
nb_repetition = int(input("Entrez le nombre de répétitions que vous souhaitez : "))

# METHOODE 1
# avec une liste de mots de la langue française
total_time1 = 0.
for repet in range(nb_repetition):
    tic1 = perf_counter()
    brute_force(mot,fichier)
    toc1 = perf_counter()
    total_time1 += toc1-tic1
# Affichage de la moyenne du temps d'exécution
print(f"Le temps d'execution moyen de la première méthode est : {(total_time1/nb_repetition)} [s]")


# METHOODE 2
# en faisant intervenir l'utilisateur
total_time2 = 0.
for repet in range(nb_repetition):
    tic2 = perf_counter()
    brute_force_methode_2(mot)
    toc2 = perf_counter()
    total_time2 += toc2-tic2
# Affichage de la moyenne du temps d'exécution
print(f"Le temps d'execution moyen de la seconde méthode est : {(total_time2/nb_repetition)} [s]")

# Donne la fonction brute force la plus efficace
if (toc2-tic2) < (toc1-tic1) :
    print("La méthode faisant intervenir l'utilisateur est plus efficace")
else :
    print("La méthode utilisant une liste de mots et ne faisant pas intervenir l'utilisateur est plus efficace")