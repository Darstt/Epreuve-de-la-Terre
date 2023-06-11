while True:
	try:
		heure_entree = input("entrez heure format HH:MM : ")
		heures, minutes = heure_entree.split(":")
		heures = int(heures)
		minutes = int(minutes)
	
	
		if heures >= 0 and heures <= 23 and minutes >= 0 and minutes <= 59:
			break
		else:
			print("heure invalide")
		
	except ValueError:
		print ("erreur format")
    
# Changement format
		
suffixe = "AM"
if heures >= 12:
    suffixe = "PM"

if heures == 0:
    heures = 12
elif heures > 12:
    heures -= 12

heure_12h = "{:02d}:{:02d} {}".format(heures, minutes, suffixe)
print("Heure introduite (format 12 heures) :", heure_12h)
