print("""OPEN CLASSROOM : Apprenez à programmer en Python
B010 Créez votre premier objet: les chaines de caractères 1/3
""")

angryell = str()
angryell = "NE CRIE PAS SI FORT !"
angryell.lower()           #""xxx.lower() renvoie la chaîne en minuscules mais ne modifie pas la chaîne"

print(angryell)

print("""--------------------------------------------------""")

yell = str()
while yell.lower() != "q":
    print("Tapez 'Q' pour quitter")
    yell = input()

print("Merci !")



print("""--------------------------------------------------""")

minus = "une phrase en minus"
minus.upper() #elle passe en maj

print(minus) # mais lorsque print elle reste en minus lors du run, mais probablement pas avec l'interpréteur

minus.capitalize() #première lettre en majuscule

print("""--------------------------------------------------""")

space = "        une      chaine avec des espaces    "
space.strip() #retrait des spaces avant et après la chaîne

print(space)

print("""--------------------------------------------------""")

title = "introduction"
title.upper().center(20) # centrage du texte dans 20 caractère

print(title)


print("""--------------------------------------------------


for Simplon
William aka wiileewaller the new coder 26/02""")
