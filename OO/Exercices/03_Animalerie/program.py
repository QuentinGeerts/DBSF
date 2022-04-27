# Animalerie
# Nous désirons effectuer la gestion d’une animalerie. 
# Cette dernière s’occupe de plusieurs types d’animaux : 
# chiens, chats, oiseaux… (laissez libre cours à votre imagination)

# Pour chaque animal, l’animalerie doit connaitre : 
# son nom, son poids, sa taille, son sexe, son âge, son âge humain équivalent et sa date d’arrivée à l’animalerie. 
# Tous les animaux possèdent le comportement crier

# Les chats doivent également être caractérisés par leur caractère (énergique, farouche, câlin, etc.), 
# si leurs griffes ont été coupées et s’il s’agit d’un chat à poil long ou non.
# Pour les chats, la probabilité de décès est de 0.5%.

# Les chiens doivent être caractérisés par la couleur de leur collier, s’il a été dressé et sa race.
# Pour les chiens, la probabilité de décès est de 1%.

# Les oiseaux, quant à eux, sont caractérisés par leur couleur et s’ils doivent vivre dans une volière ou dans une petite cage. Pour ces derniers, la probabilité de décès est de 3%.

# Le programme de gestion doit :
# – Encoder des animaux (chiens, chats, oiseaux)
# – Lister les caractéristiques de tous les animaux encodés.
# V Afficher le nombre de chats, de chiens et d’oiseaux
# – Vérifier si certains animaux ne sont pas décédés durant la nuit

import datetime
from exceptions.RefugeError import RefugeError
from models.animaux.chat import Chat
from models.animaux.chien import Chien
from models.animaux.oiseau import Oiseau
from models.animaux.animal import Animal
from models.refuge import Refuge

refuge = Refuge("DBSF", 1, "Rue du Gaucheret", 88, "Bruxelles", 1030)

chat_1 = Chat("Noirau", 400, 50, "M", datetime.date(2020, 10, 5), "Énervant", False)
chat_2 = Chat("Garfield", 1200, 60, "M", datetime.date(2005, 10, 5), "Gourmant", False)
# chat_3 = Chat()

# chien_1 = Chien()
# chien_2 = Chien()
# chien_3 = Chien()

# oiseau_1 = Oiseau()
# oiseau_2 = Oiseau()
# oiseau_3 = Oiseau()

try:
    refuge.ajouter_animal(chat_1)
    refuge.ajouter_animal(chat_2)
    refuge.ajouter_animal(refuge)
except RefugeError as re:
    print(re.message)


print(refuge.nb_chat)
