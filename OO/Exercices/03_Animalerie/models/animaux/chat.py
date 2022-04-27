# Les chats doivent également être caractérisés par leur caractère (énergique, farouche, câlin, etc.), 
# si leurs griffes ont été coupées et s’il s’agit d’un chat à poil long ou non.
# Pour les chats, la probabilité de décès est de 0.5%.

from models.animaux.animal import Animal


class Chat(Animal):
    
    # Constructeur
    def __init__(self, nom, poids, taille, sexe, date_naissance, caractere, poil_long):
        super().__init__(nom, poids, taille, sexe, date_naissance, 0.5)
        self.__caractere = caractere
        self.__poil_long = poil_long

    # Props


    # Méthodes
    def crier(self):
        print('Miaouw °w°')


    # Méthodes spéciales