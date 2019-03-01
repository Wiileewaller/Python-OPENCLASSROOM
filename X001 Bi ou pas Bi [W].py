# -*-coding:Latin-1 -*

import os

print("""

OPENCLASSROOMS 

Hello Python World !

Voici mon tout premier exo en Python ! 
Il s'agit ici de creer un code afin de savoir si l'année saisie est bisextile ou non ! """)

année = input("Saisisez une année : ")
année = int(année)

bissextile = False

if année %400 == 0:
    bissextile = True
elif année % 100 == 0:
    bissextile = False
elif année % 4 == 0:
    bisextile = True
else:
    bisextile = False

if bissextile == True:
    print("année est une année bissextile ! woohoo *.* !")
else:
    print("année n'est pas une année bissextile... snif U.U")





    print("""--------------------------------------------------


for Simplon
William aka wiileewaller the new coder 17/02""")
