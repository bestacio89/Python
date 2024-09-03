# Utiliser la fonction input pour receuillir le nom, le prénom, l'âge, et l'adresse de l'utilisateur
# Printer toutes les informations à la fin du script

nom = input("Entrez votre nom: ")
prenom = input("Entrez votre prénom: ")
age = input("Entrez votre âge: ")
adresse = input("Entrez votre adresse: ")

print(f"Nom: {nom}, Prénom: {prenom}, Âge: {age}, Adresse: {adresse}")

# Utiliser la fonction input pour demander à l'utilisateur de donner nombre entier
# Printer le chiffre donné en lui ayant préalablement ajouté 3,14

nombre = int(input("Entrez un nombre entier: "))
resultat = nombre + 3.14

print(f"Le résultat est: {resultat}")