année = input("""met ton chiffre ici --->""")

try:
    résultat = numérateur / dénominateur

except NameError:
    print("La variable numérateur ou dénominateur n'a pas été définie.")

except TypeError:
    print("La variable numérateur ou dénominateur possède un type incompatible avec la division.")

except ZeroDivisionError:
    print("La variable déminateur est égale à 0.")

except type_de_l_exception as exception_retournée
    print ("Voici l'erreur")

