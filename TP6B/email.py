class AdresseEmail:
    def __init__(self, adresse_email):
        self.adresse_email = adresse_email

class Email:
    def __init__(self, titre=None, contenu=None):
        self.titre = titre
        self.contenu = contenu
        self.destination = None  # Agrégation avec Destination
        self.expediteur = None  # Agrégation avec Expediteur
        self.fichier = []  # Composition avec Fichier

    def assigner_expediteur(self, expediteur):
        self.expediteur = expediteur

    def assigner_destination(self, destination):
        self.destination = destination

    def ajouter_fichier(self, fichier):
        self.fichier.append(fichier)

class Destination(AdresseEmail):
    def __init__(self, adresse_email):
        super().__init__(adresse_email)  # Relation d'héritage avec AdresseEmail
        self.email = []

class Expediteur(AdresseEmail):
    def __init__(self, adresse_email):
        super().__init__(adresse_email)  # Relation d'héritage avec AdresseEmail
        self.email = []


class Fichier:
    def __init__(self, nom):
        self.nom = nom

# Exemple d'utilisation :
expediteur_email = Expediteur("thierry@example.com")
destinataire_email = Destination("lafabrique@hotmail.com")

email = Email("CV", "Bonjour, \n je vous envoie mes CV")
email.assigner_expediteur(expediteur_email)
email.assigner_destination(destinataire_email)

fichier1 = Fichier("cvPersonnel.pdf")
fichier2 = Fichier("cvProfessionnel.pdf")

email.ajouter_fichier(fichier1)
email.ajouter_fichier(fichier2)

print(f"Email de {expediteur_email.adresse_email} à {destinataire_email.adresse_email}")
print(f"Titre: {email.titre}, Texte: {email.contenu}")

print(f"Fichier joint")
for fichier in email.fichier:
    print(f"- Nom du fichier: {fichier.nom}")
