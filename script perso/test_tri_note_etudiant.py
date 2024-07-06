import unittest
import os
import sys
from io import StringIO
from tri_note_etudiant import *

class TestTriNotes(unittest.TestCase):
    def setUp(self):
        # Initialisation du dictionnaire de cours avant chaque test
        self.dictionnaire_cours = dictionnaire_cours
        self.dictionnaire_cours.clear()  # Assurez-vous que le dictionnaire est vide au départ
        self.dictionnaire_etudiants = dictionnaire_etudiants
        self.dictionnaire_etudiants.clear()

    def tearDown(self):
        # Nettoyage après chaque test si nécessaire
        self.dictionnaire_cours.clear()
        self.dictionnaire_etudiants.clear()
        if os.path.exists("cours.txt"):
            os.remove("cours.txt")
        if os.path.exists("etudiants.txt"):
            os.remove("etudiants.txt")

    def test_creer_cours(self):
        cours1 = "Math"
        cours2 = "Anglais"
        cours3 = "Progra"
        cours4 = "OS"

        # Test pour cours valide
        creer_cours(cours1)
        creer_cours(cours2)
        creer_cours(cours3)
        creer_cours(cours4)

        # Vérification que les cours ont bien été ajoutés au dictionnaire
        self.assertIn(cours1, self.dictionnaire_cours)
        self.assertIn(cours2, self.dictionnaire_cours)
        self.assertIn(cours3, self.dictionnaire_cours)
        self.assertIn(cours4, self.dictionnaire_cours)

        # Vérification des noms de cours
        self.assertEqual(cours1, self.dictionnaire_cours[cours1].nom)
        self.assertEqual(cours2, self.dictionnaire_cours[cours2].nom)
        self.assertEqual(cours3, self.dictionnaire_cours[cours3].nom)
        self.assertEqual(cours4, self.dictionnaire_cours[cours4].nom)

        # Test pour un cours déjà existant
        creer_cours(cours1)
        self.assertEqual(4, len(self.dictionnaire_cours))  # Vérifie qu'il n'y a pas de doublons

        creer_cours(cours2)
        self.assertEqual(4, len(self.dictionnaire_cours))

        creer_cours(cours3)
        self.assertEqual(4, len(self.dictionnaire_cours))

        creer_cours(cours4)
        self.assertEqual(4, len(self.dictionnaire_cours))

        # Test pour un cours avec nom vide
        creer_cours("")
        self.assertNotIn("", self.dictionnaire_cours)

        # Test pour un cours avec nom non alphabétique
        creer_cours("123")
        self.assertNotIn("123", self.dictionnaire_cours)

    def test_creer_etudiant(self):
        etudiant1 = ("Doe", "John", "123")
        etudiant2 = ("Smith", "Jane", "456")
        etudiant3 = ("Williams", "Pierre-Andre", "789")

        # Test pour un étudiant valide
        creer_etudiant(*etudiant1)
        creer_etudiant(*etudiant2)
        creer_etudiant(*etudiant3)

        # Vérification que les étudiants ont bien été ajoutés au dictionnaire
        self.assertIn(etudiant1[2], self.dictionnaire_etudiants)
        self.assertIn(etudiant2[2], self.dictionnaire_etudiants)
        self.assertIn(etudiant3[2], self.dictionnaire_etudiants)

        # Vérification des matricules
        self.assertEqual(etudiant1[2], dictionnaire_etudiants[etudiant1[2]].matricule)
        self.assertEqual(etudiant2[2], dictionnaire_etudiants[etudiant2[2]].matricule)
        self.assertEqual(etudiant3[2], dictionnaire_etudiants[etudiant3[2]].matricule)

        # Test pour un étudiant déjà existant
        with self.assertRaises(ValueError):
            creer_etudiant(*etudiant1)  # Doit lever une exception
        with self.assertRaises(ValueError):
            creer_etudiant(*etudiant2)  # Doit lever une exception
        with self.assertRaises(ValueError):
            creer_etudiant(*etudiant3)  # Doit lever une exception

        # Test pour un étudiant avec nom vide
        with self.assertRaises(ValueError):
            creer_etudiant("", "Jane", "456")  # Doit lever une exception

        # Test pour un étudiant avec prénom vide
        with self.assertRaises(ValueError):
            creer_etudiant("Smith", "", "456")  # Doit lever une exception

        # Test pour un étudiant avec matricule vide
        with self.assertRaises(ValueError):
            creer_etudiant("Doe", "John", "")  # Doit lever une exception

        # Test pour un étudiant avec nom non alphabétique
        with self.assertRaises(ValueError):
            creer_etudiant("123", "Jane", "456")  # Doit lever une exception

        # Test pour un étudiant avec nom, prenom et matricule non alphabétique
        with self.assertRaises(ValueError):
            creer_etudiant(125, 150, 65)

    def test_attribuer_note(self):
        note1 = 12
        note2 = 16
        note3 = 20
        note4 = 18
        note5 = 10
        note6 = 16
        note7 = 15
        note8 = -2
        cours1 = "Anglais"
        cours2 = "Progra"
        cours3 = "Math"
        cours4 = "OS"
        etudiant1 = ("Doe", "John", "123")
        etudiant2 = ("Smith", "Jane", "456")
        etudiant3 = ("Williams", "Bob", "789")

        # Créer les étudiants et les cours nécessaires
        creer_etudiant(*etudiant1)
        creer_etudiant(*etudiant2)
        creer_etudiant(*etudiant3)
        creer_cours(cours1)
        creer_cours(cours2)
        creer_cours(cours3)
        creer_cours(cours4)

        # Attribuer les notes
        attribuer_note(note1, etudiant1[2], cours1)
        attribuer_note(note2, etudiant1[2], cours2)
        attribuer_note(note3, etudiant1[2], cours3)
        attribuer_note(note4, etudiant2[2], cours1)
        attribuer_note(note5, etudiant2[2], cours2)
        attribuer_note(note6, etudiant2[2], cours3)
        attribuer_note(note7, etudiant3[2], cours1)
        attribuer_note(note4, etudiant3[2], cours2)
        attribuer_note(note1, etudiant3[2], cours3)

        # Vérifier les notes attribuées
        self.assertEqual(note1, self.dictionnaire_cours[cours1].notes[etudiant1[2]])
        self.assertEqual(note2, self.dictionnaire_cours[cours2].notes[etudiant1[2]])
        self.assertEqual(note3, self.dictionnaire_cours[cours3].notes[etudiant1[2]])
        self.assertEqual(note4, self.dictionnaire_cours[cours1].notes[etudiant2[2]])
        self.assertEqual(note5, self.dictionnaire_cours[cours2].notes[etudiant2[2]])
        self.assertEqual(note6, self.dictionnaire_cours[cours3].notes[etudiant2[2]])
        self.assertEqual(note7, self.dictionnaire_cours[cours1].notes[etudiant3[2]])
        self.assertEqual(note4, self.dictionnaire_cours[cours2].notes[etudiant3[2]])
        self.assertEqual(note1, self.dictionnaire_cours[cours3].notes[etudiant3[2]])

        # Vérifier les cas d'erreur
        with self.assertRaises(ValueError) as context:
            attribuer_note(note1, "999", cours1)  # Étudiant inexistant
        self.assertEqual(str(context.exception), "L'étudiant avec le matricule 999 n'existe pas.")
        with self.assertRaises(ValueError) as context:
            attribuer_note(note1, etudiant1[2], "NonExistentCourse")  # Cours inexistant
        self.assertEqual(str(context.exception),
                         "Le cours NonExistentCourse n'existe pas. Veuillez créer le cours avant d'attribuer une note.")
        with self.assertRaises(ValueError) as context:
            attribuer_note(note8, etudiant1[2], cours4)  # Note négative
        self.assertEqual(str(context.exception), "La note ne peut pas être négative.")
        with self.assertRaises(ValueError) as context:
            attribuer_note(note1, etudiant1[2], cours3)  # Etudiant possédant 1 note existante
        self.assertEqual(str(context.exception),
                         f"L'étudiant avec le matricule {etudiant1[2]} a déjà une note pour le cours {cours3}.")

    def test_trier_note(self):
        etudiant1 = ("Doe", "John", "123")
        etudiant2 = ("Smith", "Jane", "456")
        etudiant3 = ("Williams", "Bob", "789")
        cours1 = "Anglais"
        cours2 = "Progra"
        note1 = 12
        note2 = 16
        note3 = 20

        # Création des étudiants (optionnelle) et des cours
        creer_etudiant(*etudiant1)
        creer_etudiant(*etudiant2)
        creer_etudiant(*etudiant3)
        creer_cours(cours1)
        creer_cours(cours2)

        # Cas de tri classique

        attribuer_note(note1, etudiant1[2], cours1)
        attribuer_note(note2, etudiant2[2], cours1)
        attribuer_note(note3, etudiant3[2], cours1)

        # Obtention du tri des notes pour le cours spécifié
        tri_notes = dictionnaire_cours[cours1].trier_notes()

        # Affichage du tri des notes (facultatif)
        print(f"Tri des notes pour le cours {cours1}: {tri_notes}")

        # Vérification des assertions
        self.assertIsInstance(tri_notes, list)
        self.assertEqual(tri_notes, [(etudiant3[2], note3), (etudiant2[2], note2), (etudiant1[2], note1)])

        # Cas de tri avec une égalité
        attribuer_note(note2, etudiant1[2], cours2)
        attribuer_note(note2, etudiant2[2], cours2)
        attribuer_note(note1, etudiant3[2], cours2)

        # Obtention du tri des notes pour le cours spécifié
        tri_notes = dictionnaire_cours[cours2].trier_notes()

        # Affichage du tri des notes (facultatif)
        print(f"Tri des notes pour le cours {cours2}: {tri_notes}")

        # Vérification des assertions
        self.assertIsInstance(tri_notes, list)
        self.assertEqual(tri_notes, [(etudiant1[2], note2), (etudiant2[2], note2), (etudiant3[2], note1)])

    # NON FONCTIONNELLE
    def test_afficher_note_triees(self):
        # Sauvegarder l'ancienne valeur de sys.stdout
        old_stdout = sys.stdout
        # Créer un objet StringIO pour capturer la sortie
        mock_stdout = StringIO()
        # Rediriger sys.stdout vers mock_stdout
        sys.stdout = mock_stdout

        try:
            # Réinitialisation des dictionnaires avant chaque test
            dictionnaire_cours.clear()
            dictionnaire_etudiants.clear()

            # Cas 1 : Aucun cours et aucun étudiant
            afficher_notes_triees()
            output_str = mock_stdout.getvalue().strip()
            assert "Aucun cours ni étudiant n'a été créé." in output_str, f"Erreur: {output_str}"
            mock_stdout.truncate(0)
            mock_stdout.seek(0)

            # Cas 2 : Aucun cours mais des étudiants créés
            creer_etudiant("Doe", "John", "123")
            afficher_notes_triees()
            output_str = mock_stdout.getvalue().strip()
            assert "Aucun cours n'a été créé." in output_str, f"Erreur: {output_str}"
            mock_stdout.truncate(0)
            mock_stdout.seek(0)

            # Cas 3 : Aucun étudiant mais des cours créés
            dictionnaire_cours.clear()  # Réinitialiser les cours
            dictionnaire_etudiants.clear()  # Réinitialiser les étudiants
            creer_cours("Anglais")
            afficher_notes_triees()
            output_str = mock_stdout.getvalue().strip()
            assert "Aucun étudiant n'a été créé." in output_str, f"Erreur: {output_str}"
            mock_stdout.truncate(0)
            mock_stdout.seek(0)

            # Cas 4 : Étudiants et cours créés mais aucune note attribuée
            creer_etudiant("Doe", "John", "123")
            creer_etudiant("Smith", "Jane", "456")
            afficher_notes_triees()
            output_str = mock_stdout.getvalue().strip()
            assert "Aucune note n'a été attribuée." in output_str, f"Erreur: {output_str}"
            mock_stdout.truncate(0)
            mock_stdout.seek(0)

            # Cas 5 : Étudiants et cours créés et 3 notes différentes attribuées
            creer_etudiant("Williams", "Bob", "789")
            attribuer_note(12, "123", "Anglais")
            attribuer_note(16, "456", "Anglais")
            attribuer_note(20, "789", "Anglais")
            afficher_notes_triees()
            output_str = mock_stdout.getvalue().strip()
            expected_output = (
                "Le cours: Anglais a été créé\n"
                "Voici la liste des cours existants:\n"
                "  - Anglais\n"
                "Cours: Anglais\n"
                "  789: 20/20 (étudiant Bob Williams)\n"
                "  456: 16/20 (étudiant Jane Smith)\n"
                "  123: 12/20 (étudiant John Doe)"
            )
            for line in expected_output.strip().split('\n'):
                assert line in output_str, f"Erreur: {line} non trouvé dans {output_str}"
            mock_stdout.truncate(0)
            mock_stdout.seek(0)

            # Cas 6 : Étudiants et cours créés et 3 notes attribuées (2 identiques et 1 différente)
            creer_cours("Progra")
            attribuer_note(16, "123", "Progra")
            attribuer_note(16, "456", "Progra")
            attribuer_note(12, "789", "Progra")
            afficher_notes_triees()
            output_str = mock_stdout.getvalue().strip()
            expected_output = (
                "Le cours: Progra a été créé\n"
                "Voici la liste des cours existants:\n"
                "  - Anglais\n"
                "  - Progra\n"
                "Cours: Progra\n"
                "  123: 16/20 (étudiant John Doe)\n"
                "  456: 16/20 (étudiant Jane Smith)\n"
                "  789: 12/20 (étudiant Bob Williams)"
            )
            for line in expected_output.strip().split('\n'):
                assert line in output_str, f"Erreur: {line} non trouvé dans {output_str}"
        finally:
            # Restaurer sys.stdout à sa valeur d'origine
            sys.stdout = old_stdout

    def test_moyenne_etudiant(self):
        expected_outputs = []

        # Cas avec 3 notes
        with self.subTest("Étudiant avec 3 notes"):
            etudiant1 = ("Doe", "John", "123")
            cours1 = "Anglais"
            cours2 = "Progra"
            cours3 = "Math"
            note1 = 12
            note2 = 16
            note3 = 20

            creer_etudiant(*etudiant1)
            creer_cours(cours1)
            creer_cours(cours2)
            creer_cours(cours3)

            attribuer_note(note1, etudiant1[2], cours1)
            attribuer_note(note2, etudiant1[2], cours2)
            attribuer_note(note3, etudiant1[2], cours3)

            old_stdout = sys.stdout
            mock_stdout = StringIO()
            sys.stdout = mock_stdout

            try:
                moyenne_etudiant(etudiant1[2])

                output_str = mock_stdout.getvalue().strip()
                expected_output = f"Moyenne des notes pour l'étudiant {etudiant1[2]}: 16.00/20"
                expected_outputs.append(expected_output)
                self.assertEqual(output_str, expected_output)
            finally:
                sys.stdout = old_stdout

        # Cas avec 2 notes (1 note à 0)
        with self.subTest("Étudiant avec 2 notes (1 note à 0)"):
            etudiant2 = ("Smith", "Jane", "456")
            cours1 = "Anglais"
            cours2 = "Progra"
            cours3 = "Math"
            note1 = 12
            note2 = 16
            # Note pour le cours Math absente ou égale à 0
            note3 = 0  # ou None, pour simuler l'absence de note

            creer_etudiant(*etudiant2)
            creer_cours(cours1)
            creer_cours(cours2)
            creer_cours(cours3)

            attribuer_note(note1, etudiant2[2], cours1)
            attribuer_note(note2, etudiant2[2], cours2)
            attribuer_note(note3, etudiant2[2], cours3)

            old_stdout = sys.stdout
            mock_stdout = StringIO()
            sys.stdout = mock_stdout

            try:
                moyenne_etudiant(etudiant2[2])

                output_str = mock_stdout.getvalue().strip()
                expected_output = f"Moyenne des notes pour l'étudiant {etudiant2[2]}: 9.33/20"
                expected_outputs.append(expected_output)
                self.assertEqual(output_str, expected_output)
            finally:
                sys.stdout = old_stdout

        # Cas étudiant sans notes
        with self.subTest("Étudiant sans notes"):
            etudiant3 = ("Brown", "Robert", "555")

            creer_etudiant(*etudiant3)

            old_stdout = sys.stdout
            mock_stdout = StringIO()
            sys.stdout = mock_stdout

            try:
                moyenne_etudiant(etudiant3[2])

                output_str = mock_stdout.getvalue().strip()
                expected_output = f"L'étudiant {etudiant3[2]} n'a aucune note attribuée."
                expected_outputs.append(expected_output)
                self.assertEqual(output_str, expected_output)
            finally:
                sys.stdout = old_stdout

        # Cas étudiant inexistant
        with self.subTest("Étudiant inexistant"):
            etudiant4 = ("Schubbert", "Michael", "999")

            old_stdout = sys.stdout
            mock_stdout = StringIO()
            sys.stdout = mock_stdout

            try:
                moyenne_etudiant(etudiant4)

                output_str = mock_stdout.getvalue().strip()
                expected_output = f"L'étudiant avec le matricule {etudiant4} n'existe pas"
                expected_outputs.append(expected_output)
                self.assertEqual(output_str, expected_output)
            finally:
                sys.stdout = old_stdout

        # Affichage des expected_outputs à la fin de tous les sous-tests
        print("\n=== Expected Outputs ===")
        for output in expected_outputs:
            print(output)

    def test_sauvegarder_et_charger_donnees(self):
        # Créer des données fictives pour tester la sauvegarde et le chargement
        etudiant1 = Etudiant("Doe", "John", "123")
        etudiant2 = Etudiant("Smith", "Jane", "456")
        etudiant3 = Etudiant("Williams", "Pierre-Andre", "789")
        cours1 = "Anglais"
        cours2 = "Progra"
        cours3 = "Math"
        note1 = 12
        note2 = 16
        note3 = 20

        creer_etudiant(etudiant1.nom, etudiant1.prenom, etudiant1.matricule)
        creer_etudiant(etudiant2.nom, etudiant2.prenom, etudiant2.matricule)
        creer_etudiant(etudiant3.nom, etudiant3.prenom, etudiant3.matricule)

        creer_cours(cours1)
        creer_cours(cours2)
        creer_cours(cours3)

        attribuer_note(note1, etudiant1.matricule, cours1)
        attribuer_note(note2, etudiant1.matricule, cours2)
        attribuer_note(note3, etudiant1.matricule, cours3)

        # Sauvegarder les données dans les fichiers
        sauvegarder_donnees()

        # Charger les données depuis les fichiers
        charger_donnees()

        # Vérifier si les données chargées sont identiques aux données sauvegardées
        self.assertEqual(dictionnaire_etudiants[etudiant1.matricule].nom, etudiant1.nom)
        self.assertEqual(dictionnaire_etudiants[etudiant2.matricule].nom, etudiant2.nom)
        self.assertEqual(dictionnaire_etudiants[etudiant3.matricule].nom, etudiant3.nom)

        self.assertEqual(dictionnaire_cours[cours1].notes[etudiant1.matricule], note1)
        self.assertEqual(dictionnaire_cours[cours2].notes[etudiant1.matricule], note2)
        self.assertEqual(dictionnaire_cours[cours3].notes[etudiant1.matricule], note3)


if __name__ == '__main__':
    unittest.main()
