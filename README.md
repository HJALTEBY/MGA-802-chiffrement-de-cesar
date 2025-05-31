# Chiffrement de César – Mini-Projet A

Projet Python réalisé dans le cadre du cours **MGA802 - Introduction à la programmation avec Python**.  
Ce programme permet d’encrypter et de décrypter des messages ou des fichiers texte selon l’algorithme classique du **code de César**.

---

## Fonctionnalités principales

- Encryptage de messages texte saisis dans le terminal
- Décryptage de messages avec clé connue
- Décryptage automatique par brute force (avec dictionnaire ou confirmation manuelle)
- Gestion d’entrées utilisateur robustes (validation, erreurs)
- Lecture et traitement de fichiers `.txt`
- Nettoyage automatique des accents pour faciliter le traitement

---

## Objectifs pédagogiques

- Implémenter un chiffrement classique (César) en Python
- Utiliser la manipulation de chaînes, fichiers, exceptions et boucles
- Concevoir une architecture modulaire (plusieurs fichiers, fonctions réutilisables)
- Collaborer efficacement via Git (branches, commits, pull requests)
- Apprendre à interagir avec l’utilisateur via le terminal

---

## Utilisation

### 1. Cloner le projet

Copiez le lien du dépôt GitHub et clonez-le dans PyCharm.

### 2. Lancer le programme

- Cliquez sur le bouton **Run**
- Choisissez si vous voulez **encrypter** ou **décrypter** un message ou un fichier

---

### Encrypter un message

- Le programme vous invite à entrer un message à encrypter via la console.
- Seule une chaîne de caractères est acceptée.
- Ensuite, entrez une **clé de cryptage** comprise entre 0 et 25.

---

### Décrypter un message

- Le programme vous invite à entrer un message à décrypter via la console.
- Les instructions à suivre s’affichent dans le terminal.
- Si vous connaissez la clé, entrez-la.

---

### Décrypter un fichier

- Le programme vous permet d’entrer le **nom d’un fichier `.txt`** à décrypter.
- Ajoutez le fichier `"nom_du_fichier.txt"` à la racine du projet (dossier `MGA-802-chiffrement-de-cesar`).
- Attention : **entrez exactement** le nom du fichier, avec l’extension `.txt`.
- Si votre fichier n’est pas à la racine, **précisez le chemin complet**.
- Si vous connaissez la clé, entrez-la.

---

### Si la clé est inconnue

Vous pouvez utiliser deux méthodes **brute-force** :

#### Méthode 1 — `brute_force` (automatique)

- Ne demande **aucune intervention** de l'utilisateur.
- L'algorithme :
  - Lit le **premier mot** du message crypté.
  - Tente toutes les clés de 0 à 26.
  - Compare chaque mot décrypté à un **dictionnaire de mots existants**.
  - Si le mot est trouvé dans le dictionnaire, la clé est considérée comme valide.
  - Sinon, on teste la clé suivante.

#### Méthode 2 — `brute_force_methode_2` (manuelle)

- Nécessite la **validation de l'utilisateur**.
- L'algorithme :
  - Lit le premier mot du message crypté.
  - Tente chaque clé et affiche le mot décrypté.
  - Demande à l’utilisateur si le mot est valide.
  - Continue jusqu’à validation ou jusqu’à épuisement des 26 clés.

---

## Remarques finales

- Si aucune clé n'est trouvée, un message approprié s'affichera.
- Assurez-vous de tester les différents cas d’usage pour valider le bon fonctionnement.

