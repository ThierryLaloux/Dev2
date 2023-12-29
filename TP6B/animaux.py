class Habitat:
    def __init__(self, nom_de_habitat):
        self.nom_de_habitat = nom_de_habitat
        self.animaux = []  # Agregation avec Animaux (multiplicité *)

    def ajout_animal(self, animal):
        self.animaux.append(animal)


class Caracteristique:
    def __init__(self, tete, corps, membre):
        self.tete = tete
        self.corps = corps
        self.membre = membre
        self.animaux = []  # Composition avec Animaux

    def ajout_animal(self, animal):
        self.animaux.append(animal)

class Animaux:
    def __init__(self, nom):
        self.nom = nom
        self.habitat = None
        self.regime = None
        self.tete = None
        self.corps = None
        self.membre = None

    def assigner_caracteristique(self, tete, corps, membre):
        self.tete = tete
        self.corps = corps
        self.membre = membre

    def assigner_habitat(self, habitat):
        self.habitat = habitat

    def assigner_regime(self, alimentation):
        self.regime = alimentation


class Alimentation:
    def __init__(self, regime):
        self.regime = regime
        self.animaux = []  # Agregation avec Animaux (multiplicité *)

    def ajout_regime(self, animal):
        self.animaux.append(animal)


# Exemple d'utilisation
habitat_campagne = Habitat("Campagne")
habitat_savane = Habitat("Savane")
regime_herbivore = Alimentation("Herbivore")
regime_carnivore = Alimentation("Carnivore")
physique_lapin = Caracteristique("Petite", "Petit", "Court")
physique_lion = Caracteristique("Grosse", "Grand", "Puissant")
animaux_lapin = Animaux("Lapin")
animaux_lion = Animaux("Lion")

habitat_campagne.ajout_animal(animaux_lapin)
habitat_savane.ajout_animal(animaux_lion)

physique_lapin.ajout_animal(animaux_lapin)
physique_lion.ajout_animal(animaux_lion)

regime_herbivore.ajout_regime(animaux_lapin)
regime_carnivore.ajout_regime(animaux_lion)

animaux_lapin.assigner_caracteristique(physique_lapin.tete, physique_lapin.corps, physique_lapin.membre)
animaux_lion.assigner_caracteristique(physique_lion.tete, physique_lion.corps, physique_lion.membre)
animaux_lapin.assigner_habitat(habitat_campagne)
animaux_lion.assigner_habitat(habitat_savane)
animaux_lapin.assigner_regime(regime_herbivore)
animaux_lion.assigner_regime(regime_carnivore)

print(f"Habitat: {habitat_campagne.nom_de_habitat}")
for animal in habitat_campagne.animaux:
    print(f"Nom: {animal.nom}, Tete: {animal.tete}, Corps: {animal.corps}, Membres: {animal.membre}")
    print(f"Regime: {regime_herbivore.regime}\n")

print(f"Habitat: {habitat_savane.nom_de_habitat}")
for animal in habitat_savane.animaux:
    print(f"Nom: {animal.nom}, Tete: {animal.tete}, Corps: {animal.corps}, Membres: {animal.membre}")
    print(f"Regime: {regime_carnivore.regime}")