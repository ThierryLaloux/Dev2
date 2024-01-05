import argparse

dictionnaire_cours = {}
dictionnaire_etudiants = {}

class Cours:
    def __init__(self, nom):
        self.nom = nom
        self.notes = {}

    def attribuer_note(self, note, matricule):
        self.notes[matricule] = note

    def trier_notes(self):
        return sorted(self.notes.items(), key=lambda item: int(item[1]), reverse=True)

class Etudiant:
    def __init__(self, nom, prenom, matricule):
        self.nom = nom
        self.prenom = prenom
        self.matricule = matricule
        self.notes = {}

    @property
    def nom_complet(self):
        return self.prenom + " " + self.nom

    def __str__(self):
        return f"étudiant {self.nom_complet} avec le matricule {self.matricule}"

def sauvegarder_donnees():
    with open('cours.txt', 'w') as f:
        for cours in dictionnaire_cours.values():
            indentation = cours.nom.count(':') * '    '
            f.write(f'{indentation}{cours.nom}\n')
            for matricule, note in cours.notes.items():
                f.write(f'{indentation}    {matricule}: {note}\n')

    with open('etudiants.txt', 'w') as f:
        for etudiant in dictionnaire_etudiants.values():
            f.write(f'{etudiant.matricule},{etudiant.nom},{etudiant.prenom}\n')

def charger_donnees():
    global dictionnaire_cours, dictionnaire_etudiants
    try:
        with open('cours.txt', 'r') as f:
            cours_lines = [line.strip() for line in f.readlines()]
            i = 0
            while i < len(cours_lines):
                line = cours_lines[i].rstrip(':')
                indentation = line[:len(line) - len(line.lstrip())]
                cours_nom = line.strip()
                i += 1
                cours = dictionnaire_cours.get(cours_nom, None)
                if cours is None:
                    cours = Cours(cours_nom)
                    dictionnaire_cours[cours_nom] = cours

                while i < len(cours_lines) and cours_lines[i].startswith(indentation + '    '):
                    line = cours_lines[i].strip()
                    matricule, note = line.split(': ')
                    cours.attribuer_note(note, matricule)
                    i += 1
    except FileNotFoundError:
        dictionnaire_cours = {}

    try:
        with open('etudiants.txt', 'r') as f:
            dictionnaire_etudiants = {ligne.split(',')[0]: Etudiant(ligne.split(',')[1], ligne.split(',')[2], ligne.split(',')[0]) for ligne in f if len(ligne.split(',')) >= 3}
    except FileNotFoundError:
        dictionnaire_etudiants = {}

def creer_cours(nom_cours):
    """
    Creer un nouveau cours pour les étudiant

    PRE: nom_cours est une string
    POST: renvoie un nouveau cours crée
    """
    if nom_cours not in dictionnaire_cours:
        cours = Cours(nom_cours)
        dictionnaire_cours[nom_cours] = cours
        print(f"Le cours: {nom_cours} a été créé")
    else:
        print(f"Le cours: {nom_cours} est déjà présent")
    print(f"Voici la liste des cours existants: {dictionnaire_cours}")

def creer_etudiant(nom, prenom, matricule):
    """
    Créer un nouvel étudiant

    PRE: nom est une string
         prenom est une string
         matricule est une string
    POST: renvoie le matricule de l'étudiant avec son nom et son prenom
    """
    if matricule not in dictionnaire_etudiants:
        etudiant = Etudiant(nom, prenom, matricule)
        dictionnaire_etudiants[etudiant.matricule] = etudiant
        print(f"L'{etudiant} a été créé")
    else:
        print(f"L'étudiant avec le matricule {matricule} a déjà été créé")
    print(f"Voici la liste des matricules des étudiants : {dictionnaire_etudiants}")

def attribuer_note(note, matricule, nom_cours):
    """
    Attribuer une note à un étudiant pour un cours

    PRE: note est une entier
         matricule est une string
         cours est une string
    POST: renvoie pour un cours, la note de l'étudiant avec son nom et prénom
    """
    if nom_cours not in dictionnaire_cours:
        creer_cours(nom_cours)

    cours = dictionnaire_cours[nom_cours]
    cours.attribuer_note(note, matricule)

    if matricule in dictionnaire_etudiants:
        print(f"La note {note} a été attribuée à l'étudiant {matricule} pour le cours {nom_cours}")
    else:
        print(f"L'étudiant avec le matricule {matricule} n'existe pas")

def trier_notes():
    """
    Trier les notes des étudiants pour un cours

    PRE: les notes des étudiants qui est un dictionnaire
    POST: renvoie un tri des notes de la plus grande à la plus petite
    """
    tri_notes = {}
    for cours in dictionnaire_cours.values():
        tri_notes[cours.nom] = cours.trier_notes()

    return tri_notes

def afficher_notes_triees():
    """
    Afficher les notes qui ont été triées pour un cours

    PRE: les notes triées pour un cours qui est une liste
    POST: renvoie un classement des notes de la plus grande à la plus petite avec le nom de l'étudiant
    """
    notes_triees = trier_notes()
    for cours, notes in notes_triees.items():
        print(f"{cours}")
        for matricule, note in notes:
            print(f"    {matricule}: {note}/20")

def main():
    parser = argparse.ArgumentParser(description='Script de gestion des notes des étudiants par cours')
    parser.add_argument('--creer_cours', metavar='nom_du_cours', type=str, help="Créer un nouveau cours")
    parser.add_argument('--creer_etudiant', metavar='nom_etudiant', type=str, help="Créer un nouvel étudiant")
    parser.add_argument('--prenom', metavar='prenom_etudiant', type=str, help="Prénom de l'étudiant")
    parser.add_argument('--matricule', metavar='matricule_etudiant', type=str, help="Matricule de l'étudiant")
    parser.add_argument('--attribuer_notes', metavar='note', type=int, help="Attribuer une note à étudiant pour un cours")
    parser.add_argument('--cours', metavar='cours', type=str, help="Cours actuel")
    parser.add_argument('--trier_notes', action='store_true', help="Trier les notes de chaque cours")
    parser.add_argument('--afficher_notes_triees', action='store_true', help="Afficher les notes triées")

    args = parser.parse_args()

    if args.creer_cours:
        creer_cours(args.creer_cours)
    elif args.creer_etudiant:
        if args.prenom and args.matricule:
            creer_etudiant(args.creer_etudiant, args.prenom, args.matricule)
        else:
            print("Erreur : Les options --prenom et --matricule sont nécessaires pour créer un étudiant.")
    elif args.attribuer_notes:
        attribuer_note(args.attribuer_notes, args.matricule, args.cours)
    elif args.trier_notes:
        trier_notes()
    elif args.afficher_notes_triees:
        afficher_notes_triees()
    else:
        print("Aucune action spécifiée. Utilisez --help pour voir les options disponibles.")

if __name__ == "__main__":
    charger_donnees()
    main()
    sauvegarder_donnees()
