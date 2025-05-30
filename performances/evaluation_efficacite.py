"""
Ce script permet de calculer l'efficacité des deux fonctions brute force créées
Pour cela, on étudie un exemple
"""

from time import perf_counter
from cryptographie import brute_force_methode_1
from cryptographie import brute_force_methode_2

# on donne le mot crypté kek, qui correspond à ici avec une clé de +2
mot = 'kek'
fichier = "../data/dict-fr-AU-DELA-common-words.ascii"


# Evaluation du temps d'exécution pour l'exemple
# Moyenne de ce temps pour un certain nombre de répétitions
nb_repetition = 1

# METHOODE 1
total_time1 = 0.
for repet in range(nb_repetition):
    tic1 = perf_counter()
    brute_force_methode_1(mot,fichier)
    toc1 = perf_counter()
    total_time1 += toc1-tic1
# Affichage de la moyenne du temps d'exécution
print(f"Le temps d'execution moyen de la première méthode est : {(total_time1/nb_repetition)} [s]")


# METHOODE 2
total_time2 = 0.
for repet in range(nb_repetition):
    tic2 = perf_counter()
    brute_force_methode_2()
    toc2 = perf_counter()
    total_time2 += toc2-tic2
# Affichage de la moyenne du temps d'exécution
print(f"Le temps d'execution moyen de la deuxième méthode est : {(total_time2/nb_repetition)} [s]")

# Donne la fonction brute force la plus efficace
if (toc2-tic2) < (toc1-tic1) :
    print('La deuxième méthode est plus efficace')
else :
    print('La première méthode est plus efficace')