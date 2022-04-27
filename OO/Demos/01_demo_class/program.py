# from package.fichier import class/fonction
from models.Calculatrice import Calculatrice, helloWorld

# Instanciation de l'objet Calculatrice
c = Calculatrice()

print(c.A)
print(c.a)

print(c.sum(2, 4))

helloWorld()