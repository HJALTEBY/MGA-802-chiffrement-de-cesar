while True:
    liste_reponse = ['yes','oui','non','no']
    cb = str(input('Connaissez-vous la combinaison ? '))
    if cb not in liste_reponse:
        print('Réponse non-valide')
    elif cb == 'no' or 'non':
        print('boute_force')
        break
    else: #la reponse est oui ou yes
        print(f'Je connais la combinaison')
        break
obj = input('Voulez-vous encrypter ou décrypter ? ')
if obj == 'encrypter':
    print('fonction encrypter')
elif obj == 'décrypter' or 'decrypter':
    print('fonction_decrypter')
else: print('La réponse est non valide')
