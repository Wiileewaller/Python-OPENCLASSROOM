

import os
from random import randrange
from math import ceil

argent = 1000
continuer_partie = True # Booléen qui est vrai tant qu'on doit continuer la partoche

print ("Vous vous installez à la table de roulette avec ", argent, "$.")

while continuer_partie:
    nombre_mise = -654

    print("Faites vos jeux !")


    while nombre_mise <1 or nombre_mise > 50:
        nombre_mise = input("Choisir un nombre entre 1 et 50 nombre voulez vous miser ? ")



        try:
            nombre_mise =int(nombre_mise)

        except ValueError:
            print("C'est pas un nombre ça l'ami !")
            nombre_mise = -656
            continue

        if  nombre_mise < 1 or nombre_mise >50:
            print("Ce nombre est pas sur la grille copain ! joue pas au con !")




    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Quel montant voulez vous miser ?")

        try:
            mise = int(mise)

        except ValueError:
            print("Vous n'avez pas saisi de nombre !")
            mise = -654
            continue

        if mise <= 0:
            print("La somme que vous avez miser est négative ou nulle. Ceci est impossible !")
        if mise > argent:
            print("Vous ne possedez que", argent, "misez moins ou passez à la banque !")

    # Le nombre et la mie on été choisis, on fait tourner la roulette !

    numérowin = randrange(50)
    print("""La roulette tourne !
                ...
                Rien ne va plus !""")

    if numérowin == nombre_mise:
        argent += mise * 7
        print("Félicitation ! Vous avez gagné", mise * 7, "$ !")

    elif numérowin % 2 == nombre_mise % 2: #nombre ils sont de la même couleur
        mise = ceil(mise * 2)
        argent += mise

        print("Vous avez misé sur la bonne couleur")

    else:
        argent -= mise
        print("Désolé l'ami ! Tray againnn")

    # La partie s'arrête si le joueur n'a plus un rond !

    if argent <= 0:
        continuer_partie = False
        print("Vous êtes ruiné, vendez votre rein !")

    else:
        print("Il vous reste", argent,"$")

        quitter = input("Souhaitez quitter le Ksino ?")
        if quitter == "oui" or quitter == "OUI" or quitter == "Oui":

            continuer_partie = False
            print("Vous quittez le casino avec", argent, "$")



