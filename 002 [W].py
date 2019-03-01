# -*-coding:Latin-1 -*

import os

print("""Hello Python World !

Time to Boucle 1er test retour en primaire !

for Simplon
William aka wiileewaller the new coder 17/02
""")


nb = input("""Saisissez votre nombre ! ---->""")
nb = int(nb)

i = -1

while i < 10:
    print(i + 1, "*", nb, "=", (i+1)* nb)
    i += 1

achain = """   for simplon"""
for tadaaa in achain:
    print(tadaaa)
    break


bchain = "zoeijzefj"
for letre in bchain:
    if letre in "aeiouy":
        print(letre)
    else:
        print("*")



print("""
by wiilewaller""")
