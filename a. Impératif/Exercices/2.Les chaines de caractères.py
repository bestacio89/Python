# Exercice 1
# Initialisez une variable avec la chaîne `Python est cool !`. Affichez la variable.
chaine1 = "Python est cool !"
print(chaine1)

# Exercice 2
# Initialisez deux variables : une avec la chaîne `C'est l'heure d'étudier Python !` utilisant des simples quotes et l'autre avec des doubles quotes. Affichez les deux variables.
chaine_simple_quotes = 'C\'est l\'heure d\'étudier Python !'
chaine_double_quotes = "C'est l'heure d'étudier Python !"
print(chaine_simple_quotes)
print(chaine_double_quotes)

# Exercice 3
# Créez une variable avec une chaîne multilignes. Assurez-vous qu'elle contient au moins trois lignes de texte. Affichez la variable.
chaine_multiligne = """Ceci est une chaîne
qui contient plusieurs
lignes de texte."""
print(chaine_multiligne)

# Exercice 4
# Affichez exactement cette phrase sans échapper les caractères spéciaux : `backslash \, double quote ", simple quote ', tabulation \t, nouvelle ligne \n`.
print(r'backslash \, double quote ", simple quote \', tabulation \t, nouvelle ligne \n')

# Exercice 5
# Affichez exactement cette phrase en échappant les caractères spéciaux : `backslash \, double quote ", simple quote ', tabulation \t, nouvelle ligne \n`.
print('backslash \\, double quote ", simple quote \', tabulation \\t, nouvelle ligne \\n')