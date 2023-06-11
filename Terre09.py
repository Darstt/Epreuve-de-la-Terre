nombre = int(input("Introduire un nombre: "))

import math

def nombre_premier(nombre):
	if nombre < 2:
		raise ValueError("Le nombre doit être supérieur ou égal à 2.")
	for diviseur in range(2, int(math.sqrt(abs(nombre))) +1):
		if nombre % diviseur == 0:
			return False
	return True

try: 
	if nombre_premier(nombre):
		print ("Oui,", nombre, "est un nombre premier")
	else:
		print ("Non,", nombre, "n'est pas un nombre premier")
except ValueError as e:
	print ("erreur")
