chaine = input("Entrez une chaîne de caractères entre guillemets : ")

if len(chaine) > 2 and chaine[0] == '"' and chaine[-1] == '"':
    nombre_caracteres = len(chaine) - 2
    print(nombre_caracteres)
    if chaine.count('"') > 2:
        print("Erreur")
elif chaine.isdigit():
    print("Erreur")
else:
    print("Erreur")
	
