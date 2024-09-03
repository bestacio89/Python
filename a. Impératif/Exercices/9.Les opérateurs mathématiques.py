### Exercice 1 : Calculs de base

# 1. Calculez la somme de 15 et 23
somme = 15 + 23
print(somme)

# 2. Soustrayez 42 de 57
soustraction = 57 - 42
print(soustraction)

# 3. Multipliez 6 par 9
multiplication = 6 * 9
print(multiplication)

# 4. Divisez 100 par 25
division = 100 / 25
print(division)

# 5. Trouvez le reste de la division de 29 par 5
reste = 29 % 5
print(reste)

# 6. Effectuez une division entière de 29 par 5
division_entiere = 29 // 5
print(division_entiere)

# 7. Calculez 2 à la puissance de 10
puissance = 2 ** 10
print(puissance)

### Exercice 2 : Opérateurs avancés avec la librairie math

import math

# 1. Calculez la racine carrée de 81
racine_carree = math.sqrt(81)
print(racine_carree)

# 2. Arrondissez 7.8 à l'entier inférieur
arrondi_inf = math.floor(7.8)
print(arrondi_inf)

# 3. Arrondissez 7.2 à l'entier supérieur
arrondi_sup = math.ceil(7.2)
print(arrondi_sup)

### Exercice 3 : Opérateurs d'assignation

# 1. Initialisez la variable a avec la valeur 10, puis ajoutez 5 à a
a = 10
a += 5
print(a)

# 2. Initialisez la variable b avec la valeur 20, puis soustrayez 7 de b
b = 20
b -= 7
print(b)

# 3. Initialisez la variable c avec la valeur 3, puis multipliez c par 4
c = 3
c *= 4
print(c)

# 4. Initialisez la variable d avec la valeur 50, puis divisez d par 2
d = 50
d /= 2
print(d)

# 5. Initialisez la variable e avec la valeur 9, puis calculez le reste de la division de e par 4
e = 9
e %= 4
print(e)

### Exercice 4 : Opérateurs de comparaison

# 1. Vérifiez si 15 est supérieur à 10
print(15 > 10)

# 2. Vérifiez si 8 est inférieur ou égal à 8
print(8 <= 8)

# 3. Vérifiez si 20 est égal à 25
print(20 == 25)

# 4. Vérifiez si 30 est différent de 30
print(30 != 30)

# 5. Vérifiez si "Bonjour" est identique à "bonjour"
print("Bonjour" == "bonjour")

### Exercice 5 : Opérateur d'appartenance

# 1. Vérifiez si le caractère 'a' est présent dans la chaîne "programmation"
print('a' in "programmation")

# 2. Vérifiez si le mot "Python" est présent dans la phrase "Le Python est un langage génial"
print("Python" in "Le Python est un langage génial")

# 3. Vérifiez si le nombre 5 est présent dans la liste [1, 2, 3, 4, 6]
print(5 in [1, 2, 3, 4, 6])

# 4. Vérifiez si la lettre 'z' est absente de la chaîne "éducation"
print('z' not in "éducation")

# 5. Vérifiez si le nombre 10 n'est pas dans la liste [2, 4, 6, 8]
print(10 not in [2, 4, 6, 8])