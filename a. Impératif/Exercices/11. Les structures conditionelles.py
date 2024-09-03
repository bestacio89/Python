# Demander à l'utilisateur de taper un nombre
# Si celui-ci est pair, printer "Vous avez entré un nombre pair."
# Si celui-ci est impair, printer "Vous avez entré un nombre impair."
# Si l'information entrée n'est pas un nombre printer "Vous devez entrer un nombre!"

nombre = input("Entrez un nombre: ")

if nombre.isdigit():
    nombre = int(nombre)
    if nombre % 2 == 0:
        print("Vous avez entré un nombre pair.")
    else:
        print("Vous avez entré un nombre impair.")
else:
    print("Vous devez entrer un nombre!")

# Demander à un utilisateur de taper un mot
# Si celui-ci possède la lettre e OU la lettre a printer "Beep"
# Si celui-ci possède la lettre e OU la lettre a, mais sans que les deux conditions soit vraies en même temps, printer "Boop"

mot = input("Entrez un mot: ")

if 'e' in mot and 'a' in mot:
    print("Beep")
elif 'e' in mot or 'a' in mot:
    print("Boop")
else :
    print("Bam")

# A l'aide d'un match case et d'une boucle, printer "RGB" lorsque la couleur présente dans la liste suivante est une couleur au format RGB (Red Green Blue), et printer "RGBA" lorsque la couleur est au format RGBA (Red Green Blue Alpha).

# Si r, g, et b sont égaux à 0 (quelque soit le format de la couleur), alors il faudra printer "Couleur noire" en priorité seulement si la valeur d'alpha (si elle existe) est supérieure à 0

# Si r, g, et b sont égaux à 255 (quelque soit le format de la couleur), alors il faudra printer "Couleur blanche" en priorité seulement si la valeur d'alpha (si elle existe) est supérieure à 0

# Résultat attendu: RGB RGBA RGB de couleur noire RGBA RGBA RGBA de couleur blanche RGBA

colors = [(12, 72, 89), (23, 77, 200, 1), (0, 0, 0), (123, 123, 67, 1), (255, 255, 255, 0), (255, 255, 255, 1), (0, 0, 0, 0)]

for color in colors:
    match color:
        case (0, 0, 0, alpha) if alpha > 0:
            print("RGBA de Couleur noire")
        case (255, 255, 255, alpha) if alpha > 0:
            print("RGBA de Couleur blanche")
        case (r, g, b, a):
            print("RGBA")
        case (0, 0, 0):
            print("Couleur noire")
        case (255, 255, 255):
            print("Couleur blanche")
        case (r, g, b):
            print("RGB")

