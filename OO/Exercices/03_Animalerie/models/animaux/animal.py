# V Pour chaque animal, l’animalerie doit connaitre : 
# V son nom, son poids, sa taille, son sexe, son âge, son âge humain      
#   équivalent et sa date d’arrivée à l’animalerie. 
#   Tous les animaux possèdent le comportement crier
from abc import ABC, abstractmethod
from datetime import datetime, date

class Animal (ABC):

    # Constructeur
    def __init__(self, nom, poids, taille, sexe, date_naissance, chance_deces):
        self.__nom = nom
        self.__poids = poids
        self.__taille = taille
        self.__sexe = sexe if sexe is not None else "X"
        self.__date_naissance = date_naissance
        self.__date_arrivee = date.today()
        self.__est_vivant = True
        self.__est_adopte = False
        self.__chance_deces = chance_deces

    # Props
    @property
    def nom(self):
        return self.__nom
    
    @property
    def poids(self):
        return self.__poids

    # Méthodes
    @abstractmethod
    def crier(self):
        pass

    # Méthodes spéciales
