# La classe Maison possède : une adresse, une surface, un nombre de pièces et
# une surface de jardin. Elle possède une méthode resumer() qui décrira la 
# maison.
# EDIT : un nombre d'étages, nombre de garage (facultatif)

class Maison:

    def __init__(self, adresse, surface, nb_piece, surface_jardin) -> None:
        self.__adresse = adresse
        self.__surface = surface
        self.__nb_piece = nb_piece
        self.__surface_jardin = surface_jardin

    # Getters & Setters

    # Adresse
    @property
    def adresse(self):
        return self.__adresse

    @adresse.setter
    def adresse(self, nouvelle_adresse):
        self.__adresse = nouvelle_adresse

    # Surface
    @property
    def surface(self):
        return self.__surface

    @surface.setter
    def surface(self, nouvelle_surface):
        self.__surface = nouvelle_surface
    
    @property
    def nb_piece(self):
        return self.__nb_piece

    @nb_piece.setter
    def nb_piece(self, nouvelle_nb_piece):
        self.__nb_piece = nouvelle_nb_piece
    
    @property
    def surface_jardin(self):
        return self.__surface_jardin

    @surface_jardin.setter
    def surface_jardin(self, nouvelle_surface_jardin):
        self.__surface_jardin = nouvelle_surface_jardin

    def resumer(self):
        msg = f"Cette maison se situe à l'adresse : {self.adresse.format()}\n"
        msg += f"Elle a {self.nb_piece} pièce{'s' if self.nb_piece > 1 else ''}\n"

        if self.surface_jardin > 0:
            msg += f"et un jardin de {self.surface_jardin} m²."
        else:
            msg += f"sans jardin."

        return msg