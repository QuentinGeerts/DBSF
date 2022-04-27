from exceptions.RefugeError import RefugeError
from models.adresse import Adresse
from models.animaux.animal import Animal
from models.animaux.chien import Chien
from models.animaux.chat import Chat
from models.animaux.oiseau import Oiseau


class Refuge:
    
    # Constructeur
    def __init__(self, nom, capacite, rue, numero, ville, code_postal):
        self.__nom = nom
        self.__adresse = Adresse(rue, numero, ville, code_postal)
        self.__capacite = capacite        
        self.__animaux = list()

    # Props
    @property
    def nom(self):
        return self.__nom

    @property
    def adresse(self):
        return self.__adresse

    @property
    def capacite(self):
        return self.__capacite

    @capacite.setter
    def capacite(self, value):
        self.__capacite = value

    @property
    def nb_chien(self):
        nb = 0
        for animal in self.__animaux:
            if isinstance(animal, Chien):
                nb += 1
        return nb
    
    @property
    def nb_chat(self):
        nb = 0
        for animal in self.__animaux:
            if isinstance(animal, Chat):
                nb += 1
        return nb
    
    @property
    def nb_oiseau(self):
        nb = 0
        for animal in self.__animaux:
            if isinstance(animal, Oiseau):
                nb += 1
        return nb

    # Méthodes
    def resumer(self):
        description = "Liste des animaux :"

        return description

    def ajouter_animal(self, animal):
        if not isinstance(animal, Animal):
            raise RefugeError("Ce n'est pas un animal")
        
        if len(self.__animaux) + 1 > self.capacite:
            raise RefugeError("Capacité maximale atteinte.") 

        self.__animaux.append(animal)

    # Méthodes spéciales