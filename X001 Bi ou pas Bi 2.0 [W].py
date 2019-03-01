# -*-coding:Latin-1 -*

import os


print("""Hello Python World !

Optimisation du premier code! Attention optimisation de ouf !!!!!

for Simplon
William aka wiileewaller the new coder 17/02
""")


année = input("Saisissez une année:")
année =int(année)

if année %400 == 0 or (année %4 == 0 and année %100 != 0):
    print ("""L'année saisie est bi !""")
else:
    print ("""L'année saisie n'est pas bi !""")