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

# METHOODE 1
# Evaluation du temps d'exécution pour l'exemple
# Moyenne de ce temps pour 100 executions
nb_repetition = 1
total_time = 0.
for repet in range(nb_repetition):
    tic1 = perf_counter()
    brute_force_methode_1(mot,fichier)
    toc1 = perf_counter()
    total_time += toc1-tic1
# Affichage de la moyenne du temps d'exécution
print(f"Le temps d'execution moyen de la première méthode est : {(total_time/nb_repetition)} [s]")


# METHOODE 2
# Evaluation du temps d'exécution pour l'exemple
# Moyenne de ce temps pour 100 executions
nb_repetition = 1
total_time = 0.
for repet in range(nb_repetition):
    tic2 = perf_counter()
    brute_force_methode_2()
    toc2 = perf_counter()
    total_time += toc2-tic2
# Affichage de la moyenne du temps d'exécution
print(f"Le temps d'execution moyen de la deuxième méthode est : {(total_time/nb_repetition)} [s]")

if toc2-tic2 < toc1-tic1 :
    print('La deuxième méthode est plus efficace')
else :
    print('La première méthode est plus efficace')