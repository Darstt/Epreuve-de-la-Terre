nombre = input("Entrez un nombre : ")

if nombre.lstrip('-').isdigit():
    nombre = int(nombre)
    if nombre % 2 == 0:
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")
else:
    print("Tu me la mets pas à l'envers.")
