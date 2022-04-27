# Exercice 02 - Maison
# ----------------------
# - Adresse
# - Maison
# ----------------------
# La classe Maison possède : une adresse, une surface, un nombre de pièces et
# une surface de jardin. Elle possède une méthode resumer() qui décrira la 
# maison.
# EDIT : un nombre d'étages, nombre de garage (facultatif)

# La classe Adresse possède une rue, un numéro, une ville et un code postal
# EDIT : une boite (facultative). 
# Elle possède une méthode : format()
# La méthode format décrit l'adresse (rue + numéro [boite], CP + ville)

# Un programme principal : Créer les deux objets (adresse + maison) et 
# afficher les informations

# Ajouter pour tous les attributs, les ascesseurs et mutateurs. (décorateurs)
from models.adresse import Adresse
from models.maison import Maison

adresse1 = Adresse("Rue Bois de Virelles", 9, "Virelles", 6461)
maison = Maison(adresse1, 40, 5, 1200)

print(maison.resumer())
