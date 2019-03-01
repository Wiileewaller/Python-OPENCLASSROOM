print("""OPEN CLASSROOM : Apprenez à programmer en Python
B011 Créez votre premier objet: les chaines de caractère 2/3
""")


nom = """Peugeot"""
prénom = "Mégane"
année = 2006

ph1 = "Hello, je suis une petite {0} {1} et j'ai été présentée pour la première fois en {2}. "\
      .format(nom,prénom,année)

print(ph1)

print("""--------------------------------------------------""")

ph2 = """Hello again, My name is {1} {1} and i was released in {2}.""".format(nom,prénom,année)
print(ph2)

print("""--------------------------------------------------""")

jour = "Dimanche"
date = "24"
mois = "juillet"
année = "2006"
heure ="5:26"

ph3 = """Cela s'est produit le {} {} {} {}, à {}."""\
    .format(jour,date,mois,année,heure)
print(ph3)

print("""--------------------------------------------------""")


adresse = """{numrue} {nomrue}, {copostal} {ville} {pays}"""\
    .format(numrue="5",\
            nomrue="rue Saint Nestor",\
            copostal="69008",\
            ville="LYON",\
            pays="""FRANCE""")

print("""Monsieur GILBERT domicilié à""", adresse, """
accepte de prendre pour épouse Joséphine.""")

print("""--------------------------------------------------""")

fullchain = ph1 + ph3
print(fullchain)





print("""--------------------------------------------------


for Simplon
William aka wiileewaller the new coder 26/02""")