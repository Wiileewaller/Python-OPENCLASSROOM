# -*-coding:Latin-1 -*

import os

print("""

OPENCLASSROOMS 

Hello Python World !

Voici mon tout premier exo en Python ! 
Il s'agit ici de creer un code afin de savoir si l'ann�e saisie est bisextile ou non ! """)

ann�e = input("Saisisez une ann�e : ")
ann�e = int(ann�e)

bissextile = False

if ann�e %400 == 0:
    bissextile = True
elif ann�e % 100 == 0:
    bissextile = False
elif ann�e % 4 == 0:
    bisextile = True
else:
    bisextile = False

if bissextile == True:
    print("ann�e est une ann�e bissextile ! woohoo *.* !")
else:
    print("ann�e n'est pas une ann�e bissextile... snif U.U")





    print("""--------------------------------------------------


for Simplon
William aka wiileewaller the new coder 17/02""")
