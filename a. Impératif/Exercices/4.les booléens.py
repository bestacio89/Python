# Exercice 1
# Les booléens en Python peuvent seulement avoir deux valeurs possibles : True ou False.
bool1 = True
bool2 = False
print(bool1, bool2)

# Exercice 2
# En Python, la valeur True est équivalente à 1 et la valeur False est équivalente à 0.
print(int(True), int(False))

# Exercice 3
# On peut utiliser des opérations arithmétiques avec des booléens en Python, comme l'addition.
print(True + True)  # 2
print(True + False)  # 1
print(False + False)  # 0

# Exercice 4
# La fonction bool() retourne False pour une chaîne vide ("").
print(bool(""))  # False

# Exercice 5
# La fonction bool() retourne True pour tout entier différent de zéro.
print(bool(1))  # True
print(bool(0))  # False

# Exercice 6
# Un nombre décimal égal à 0.0 est considéré comme False par la fonction bool().
print(bool(0.0))  # False
print(bool(0.1))  # True

# Exercice 7
# Une liste vide ([]) est considérée comme False par la fonction bool().
print(bool([]))  # False
print(bool([1, 2, 3]))  # True

# Exercice 8
# Un dictionnaire vide ({}) est considéré comme True par la fonction bool().
print(bool({}))  # False
print(bool({"key": "value"}))  # True