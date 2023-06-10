a = int(input("Introduire le divident:"))
b = int(input("Introduire le diviseur:"))
Resultat = a//b
Reste = a % b

if b > a:
	print('error')
elif b == 0:
	print('error')
else:
	print (Resultat)
	print (Reste)
