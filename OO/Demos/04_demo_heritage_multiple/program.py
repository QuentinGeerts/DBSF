from models.voiture_amphibie import VoitureAmphibie

va = VoitureAmphibie("rouge", "electrique", 4)

va.avancer()
va.change_mode()
va.tourner()
va.accoster("Anvers")
va.change_mode()
va.accoster("Anvers")