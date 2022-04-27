class Voiture:

    def __init__(self) -> None:
        self.__roues = 4

    # Ascesseur = Récupérer
    # def _get_roue(self):
    #     return self.__roue # Retourner la valeur demandée

    # # Mutateur = Modifier
    # def _set_roue(self, value):
    #     self.__roue = value # Modifier la valeur

    # # roue = property(_get_roue, _set_roue)
    # roue = property(_get_roue)

    @property
    def roues(self):
        return self.__roues

    @roues.setter
    def roues(self, value):
        self.__roues = value