# -*-coding:Latin-1 -*

import os


print("""Hello Python World !

Optimisation du premier code! Attention optimisation de ouf !!!!!

for Simplon
William aka wiileewaller the new coder 17/02
""")


ann�e = input("Saisissez une ann�e:")
ann�e =int(ann�e)

if ann�e %400 == 0 or (ann�e %4 == 0 and ann�e %100 != 0):
    print ("""L'ann�e saisie est bi !""")
else:
    print ("""L'ann�e saisie n'est pas bi !""")