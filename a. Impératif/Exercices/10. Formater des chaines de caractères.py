# À partir des variables suivantes, et sans les modifier, formater la chaîne suivante pour obtenir le résultat suivant :
# "Bonjour, je m'appelle Bobby, j'ai 0030 ans, je suis né le May 26 1992."

# Printer la phrase

from datetime import date

prenom = "bobby"
age = 30
date_naissance = date(1992, 5, 26)

# Formater la chaîne pour obtenir le résultat souhaité
formatted_string = f"Bonjour, je m'appelle {prenom.capitalize()}, j'ai {age:04d} ans, je suis né le {date_naissance:'%B %d %Y'}."

# Imprimer la phrase
print(formatted_string)