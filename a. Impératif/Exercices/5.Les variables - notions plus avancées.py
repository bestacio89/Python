# Question 1 : Utilisation de la fonction `id()`
# Initialisez une variable `x` avec une valeur entière.
x = 420
# Utilisez la fonction `id()` pour afficher l'identifiant de `x`.
print(id(x))

# Question 2 : Passage par référence
# Déclarez une variable `a` et assignez-lui une valeur entière.
a = 10
# Affectez la valeur de `a` à une nouvelle variable `b`. Affichez leurs identifiants.
b = a
print(id(a), id(b))
# Modifiez la valeur de `a` et vérifiez si les identifiants de `a` et `b` sont toujours les mêmes.
a = 20
print(id(a), id(b))

# Question 3 : Affectations multiple et parallèles
# Initialisez deux variables `message1` et `message2` avec des chaînes de caractères différentes en même temps.
message1, message2 = "Bonjour", "Au revoir"
# Utilisez l'affectation parallèle pour échanger les valeurs de `message1` et `message2`.
message1, message2 = message2, message1
# Affichez les valeurs de `message1` et `message2` pour vérifier l'échange.
print(message1, message2)