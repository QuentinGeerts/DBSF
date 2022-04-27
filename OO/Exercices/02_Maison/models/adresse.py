# La classe Adresse possède une rue, un numéro, une ville et un code postal
# EDIT : une boite (facultative). 
# Elle possède une méthode : format()
# La méthode format décrit l'adresse (rue + numéro [boite], CP + ville)

class Adresse:

    def __init__(self, rue, numero, ville, cp, boite = None):
        self.__rue = rue
        self.__numero = numero
        self.__ville = ville
        self.__cp = cp
        self.__boite = boite

    @property
    def rue(self):
        return self.__rue
    
    @rue.setter
    def rue(self, value):
        self.__rue = value

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def ville(self):
        return self.__ville
    
    @ville.setter
    def ville(self, value):
        self.__ville = value

    @property
    def cp(self):
        return self.__cp
    
    @cp.setter
    def cp(self, value):
        self.__cp = value

    @property
    def boite(self):
        return self.__boite
    
    @boite.setter
    def boite(self, value):
        self.__boite = value

    def format(self):
        msg = f"{self.rue}, n°{self.numero}"

        if self.boite: # petite astuce => si elle existe => true
            msg += f", bte {self.boite}"

        msg += f"\n{self.cp} {self.ville}"
        return msg
    