print("""OPEN CLASSROOM : Apprenez à programmer en Python
B012 Créez votre premier objet: les chaines de caractère 3/3
""")

thefirstlist = list(["A","B","C","D","E"])
thesecondlist = [1,2,3,4,5]
thethirdlist = []
shindlerlist = [2.5, 5 , "spiderpig", 'Z', 'X', [] ]

print("class of thefirstlist:",type(thefirstlist))
print(thefirstlist)

print("class of secondlist:",type(thesecondlist))
print(thesecondlist)

print("class of thirdlist:", type(thethirdlist))
print(thethirdlist)

print("class of shindlerlist:", type(shindlerlist))
print(shindlerlist)
shindlerlist [3] = "ici"
print(shindlerlist)

thefirstlist.insert(3,'C4')
print("insert c4 in thefirstlist",thefirstlist)


thesecondlist.append("spidercat")
print("added spidercat to the secondlist",thesecondlist)


megalist = shindlerlist + thesecondlist
print("megalist =",megalist)



#A REVOIR
#gigalist = thefirstlist.extend(thesecondlist[2])   #essai d'ajout une partie de liste à une liste A VOIR
#print("gigalist =",thefirstlist)


gigalist = thefirstlist + thesecondlist[5:]
print("gigalist =",gigalist)

del thesecondlist[5]
print("thesecondlist =",thesecondlist)


print(thefirstlist)
thefirstlist.remove("C4")
print("thefirstlist =",thefirstlist)

print("""--------------------------------------------------""")

print(shindlerlist)
i=0

while i <len(shindlerlist):
    print(shindlerlist[i])
    i += 1

print(gigalist)
for elt in gigalist:
    print(elt)

print("""--------------------------------------------------"""





#RECACAP

# del           del variableX           del variable[X]
# remove        X.remove(2)
# insert        X.insert(5, 'FF')
# append        X.append("FF")
# extend        X.extend(listeX)
# +=            liste1 += liste2


print("""--------------------------------------------------


for Simplon
William aka wiileewaller the new coder 26/02""")