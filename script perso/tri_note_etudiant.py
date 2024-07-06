import cmd

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

    def __repr__(self):
        return f"Cours (nom='{self.nom}')"
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

    def __repr__(self):
        return f"Etudiant(nom='{self.nom}', prenom='{self.prenom}', matricule='{self.matricule}')"
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
    except ValueError as e:
        print("Erreur lors de la lecture du fichier cours.txt :", e)

    try:
        with open('etudiants.txt', 'r') as f:
            dictionnaire_etudiants = {ligne.split(',')[0]: Etudiant(ligne.split(',')[1], ligne.split(',')[2], ligne.split(',')[0]) for ligne in f if len(ligne.split(',')) >= 3}
    except FileNotFoundError:
        dictionnaire_etudiants = {}
    except ValueError as e:
        print("Erreur lors de la lecture du fichier etudiants.txt :", e)

def creer_cours(nom_cours):
    """
    Creer un nouveau cours pour les étudiant

    PRE: nom_cours est une string
    POST: renvoie un nouveau cours crée
    """
    try:
        if not isinstance(nom_cours, str) or not nom_cours.isalpha():
            raise ValueError("Le nom du cours doit être une chaîne de caractères alphabétiques non vide.")

        if nom_cours in dictionnaire_cours:
            print(f"Le cours: {nom_cours} est déjà présent")
            print("Voici la liste des cours existants:")
            for cours in dictionnaire_cours:
                print(f"  - {cours}")
            return

        dictionnaire_cours[nom_cours] = Cours(nom_cours)
        print(f"Le cours: {nom_cours} a été créé")
        print("Voici la liste des cours existants:")
        for cours in dictionnaire_cours:
            print(f"  - {cours}")
    except ValueError as e:
        print(f"Erreur : {e}")

def creer_etudiant(nom, prenom, matricule):
    """
    Créer un nouvel étudiant

    PRE: nom est une string
         prenom est une string
         matricule est une string
    POST: affiche un message indiquant la création de l'étudiant et met à jour le dictionnaire d'étudiants
    RAISES: ValueError si le nom ou prénom est vide, si le matricule n'est pas numérique,
            si le nom ou prénom contient autre chose que des lettres alphabétiques,
            ou si le matricule existe déjà dans le dictionnaire d'étudiants
    """
    try:
        if not isinstance(nom, str) or not isinstance(prenom, str) or not isinstance(matricule, str):
            raise ValueError("Le nom, prénom et matricule doivent être des chaînes de caractères.")

        if not nom.strip() or not prenom.strip():
            raise ValueError("Le nom et prénom ne doivent pas être vides.")

        if not nom.replace("-", "").replace(" ", "").isalpha() or not prenom.replace("-", "").replace(" ",
                                                                                                      "").isalpha():
            raise ValueError("Le nom et prénom doivent contenir uniquement des lettres alphabétiques.")

        if not matricule.isdigit():
            raise ValueError("Le matricule doit être une chaîne numérique.")

        if matricule in dictionnaire_etudiants:
            raise ValueError(f"L'étudiant avec le matricule {matricule} a déjà été créé")

        etudiant = Etudiant(nom, prenom, matricule)
        dictionnaire_etudiants[matricule] = etudiant  # Utilisation de matricule comme clé
        print(f"L'étudiant {etudiant.nom_complet} avec le matricule {etudiant.matricule} a été créé")
        print("Voici la liste des matricules des étudiants :")
        for mat in dictionnaire_etudiants.keys():
            print(f"  - {mat}")

    except ValueError as e:
        print(f"Erreur : {e}")
        raise  # Re-lève l'exception pour que les tests ou le programme principal la gèrent correctement

def attribuer_note(note, matricule, nom_cours):
    """
    Attribuer une note à un étudiant pour un cours

    PRE: note est un entier
         matricule est une chaîne de caractères
         nom_cours est une chaîne de caractères
    POST: attribue la note à l'étudiant pour le cours spécifié
    RAISES: ValueError si l'étudiant n'existe pas, le cours n'existe pas,
            la note est négative ou l'étudiant a déjà une note pour ce cours
    """
    try:
        note = int(note)
        if note < 0:
            raise ValueError("La note ne peut pas être négative.")

        if matricule not in dictionnaire_etudiants:
            raise ValueError(f"L'étudiant avec le matricule {matricule} n'existe pas.")

        cours = dictionnaire_cours.get(nom_cours)
        if cours is None:
            raise ValueError(f"Le cours {nom_cours} n'existe pas. Veuillez créer le cours avant d'attribuer une note.")

        if matricule in cours.notes:
            raise ValueError(f"L'étudiant avec le matricule {matricule} a déjà une note pour le cours {nom_cours}.")

        cours.attribuer_note(note, matricule)
        print(f"La note {note} a été attribuée à l'étudiant {matricule} pour le cours {nom_cours}.")

    except ValueError as e:
        print(f"Erreur : {e}")
        raise  # Re-lève l'exception pour une gestion globale dans le test unitaire ou le programme principal

def trier_notes():
    """
    Trier les notes des étudiants pour ce cours

    PRE: -
    POST: retourne un dictionnaire trié des notes pour ce cours, de la plus grande à la plus petite
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
    # Cas où il n'y a ni cours ni étudiant
    if not dictionnaire_cours and not dictionnaire_etudiants:
        print("Aucun cours ni étudiant n'a été créé.")
        return

    # Cas où il n'y a aucun cours
    if not dictionnaire_cours:
        print("Aucun cours n'a été créé.")
        return

    # Cas où il n'y a aucun étudiant
    if not dictionnaire_etudiants:
        print("Aucun étudiant n'a été créé.")
        return

    notes_exist = False

    # Vérifier s'il y a des cours avec des notes attribuées
    for cours in dictionnaire_cours.values():
        if cours.notes:
            notes_exist = True
            print(f"Le cours: {cours.nom} a été créé")
            print("Voici la liste des cours existants:")
            for nom in sorted(dictionnaire_cours):
                print(f"  - {nom}")

            print(f"Cours: {cours.nom}")
            for matricule, note in cours.trier_notes():
                etudiant = dictionnaire_etudiants.get(matricule)
                etudiant_nom = etudiant.nom_complet if etudiant else "Inconnu"
                print(f"  {matricule}: {note}/20 (étudiant {etudiant_nom})")

    if not notes_exist:
        print("Aucune note n'a été attribuée.")

def moyenne_etudiant(matricule):
    """
    Calculer la moyenne des notes de tous les cours pour un étudiant donné

    PRE: matricule est une string correspondant au matricule de l'étudiant
    POST: affiche la moyenne des notes pour l'étudiant
    """
    if matricule not in dictionnaire_etudiants:
        print(f"L'étudiant avec le matricule {matricule} n'existe pas")
        return

    total_notes = 0
    nb_courses = 0
    for cours in dictionnaire_cours.values():
        if matricule in cours.notes:
            total_notes += int(cours.notes[matricule])
            nb_courses += 1

    if nb_courses > 0:
        moyenne = total_notes / nb_courses
        print(f"Moyenne des notes pour l'étudiant {matricule}: {moyenne:.2f}/20")
    else:
        print(f"L'étudiant {matricule} n'a aucune note attribuée.")

class GestionNotesShell(cmd.Cmd):
    intro = "Bienvenue dans le shell de gestion des notes. Tapez ? ou help pour lister les commandes disponibles."
    prompt = "GestionNotes> "

    def do_creer_cours(self, arg):
        """Créer un nouveau cours : creer_cours nom_du_cours"""
        if arg:
            creer_cours(arg)
        else:
            print("Erreur : Le nom du cours est nécessaire.")

    def do_creer_etudiant(self, arg):
        """Créer un nouvel étudiant : creer_etudiant nom"""
        if arg:
            prenom = input("Entrez le prénom de l'étudiant: ")
            matricule = input("Entrez le matricule de l'étudiant: ")
            creer_etudiant(arg, prenom, matricule)
        else:
            print("Erreur : Le nom de l'étudiant est nécessaire.")

    def do_attribuer_note(self, arg):
        """Attribuer une note à un étudiant pour un cours : attribuer_note matricule cours note"""
        args = arg.split()
        if len(args) != 3:
            print("Erreur : Veuillez fournir un matricule, un cours et une note.")
            return
        matricule, nom_cours, note = args
        try:
            note = int(note)
            if note < 0:
                print("Erreur : La note doit être un entier positif ou nul.")
                return
        except ValueError:
            print("Erreur : La note doit être un nombre entier.")
            return
        attribuer_note(note, matricule, nom_cours)

    def do_trier_notes(self, arg):
        """
        Trier les notes des étudiants pour tous les cours.
        """
        # Pour montrer que la fonction trie les notes mais pas utile vu que afficher_notes_triees le fais déjà
        notes_triees = trier_notes()
        if not notes_triees:
            print("Aucun cours n'existe actuellement.")
        else:
            for cours, notes in notes_triees.items():
                print(f"{cours}")
                for matricule, note in notes:
                    print(f"    {matricule}: {note}/20")

    def do_afficher_notes_triees(self, arg):
        """Afficher les notes triées pour chaque cours : afficher_notes_triees"""
        afficher_notes_triees()

    def do_moyenne_etudiant(self, arg):
        """Afficher les moyennes pour chaque étudiant : moyenne_etudiant matricule"""
        if not arg:
            print("Erreur : Veuillez fournir un matricule d'étudiant.")
            return
        moyenne_etudiant(arg)

    def do_exit(self, arg):
        """Quitter le programme : exit"""
        sauvegarder_donnees()
        print("Données sauvegardées. Au revoir!")
        return True

    def do_quit(self, arg):
        return self.do_exit(arg)

    def postcmd(self, stop, line):
        print()  # Ajout d'une ligne vide après chaque commande
        return stop

def main():
    charger_donnees()
    shell = GestionNotesShell()
    shell.cmdloop()


if __name__ == "__main__":
    main()
