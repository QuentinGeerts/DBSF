from models.femme import Femme
from models.homme import Homme
from models.personne import Personne

h = Homme('Geerts', 'Quentin', 1)
f = Femme('Geerts', 'Mélanie', False)

print(isinstance(f, Femme))     # True
print(isinstance(f, Personne))  # True
print(isinstance(f, Homme))     # False
