class Personne:
    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

class Professeur(Personne):
    def __init__(self, nom, prenom, adresse):
        super().__init__(nom, prenom, adresse)  # relation d'heritage avec Personne
        self.classe = []


class Eleve(Personne):
    def __init__(self, nom, prenom, adresse):
        super().__init__(nom, prenom, adresse)  # relation d'héritage avec Personne
        self.classe = []


class Classe:
    def __init__(self, nom):
        self.nom = nom
        self.professeur = None  # Agrégation avec Professeur
        self.eleves = []  # Agrégation avec Eleve (multiplicité *)

    def assigner_professeur(self, professeur):
        self.professeur = professeur

    def ajouter_eleve(self, eleve):
        self.eleves.append(eleve)

# Exemple d'utilisation
prof = Professeur("Dupond", "Alfred", "Baker Street, 8")
eleve1 = Eleve("Bonnet", "Louis", "Garden Street, 95")
eleve2 = Eleve("Boulard", "Thierry", "rue du Cancre, 22")

classe1 = Classe("CM2")
classe1.assigner_professeur(prof)
classe1.ajouter_eleve(eleve1)
classe1.ajouter_eleve(eleve2)

print(f"Classe1: {classe1.nom}")
print(f"Prof: {prof.nom} {prof.prenom}, Adresse: {prof.adresse}")
print(f"eleve1: {eleve1.nom} {eleve1.prenom}, Adresse: {eleve1.adresse}")
print(f"eleve2: {eleve2.nom} {eleve2.prenom}, Adresse: {eleve2.adresse}")