import unittest
from tri_note_etudiant import *

class TestGestionNotes(unittest.TestCase):
    def test_creer_cours(self):
        cours1 = "Math"
        cours2 = "Anglais"
        cours3 = "Progra"
        creer_cours(cours1)
        creer_cours(cours2)
        creer_cours(cours3)
        self.assertEqual(cours1, dictionnaire_cours[cours1].nom)
        self.assertEqual(cours2, dictionnaire_cours[cours2].nom)
        self.assertEqual(cours3, dictionnaire_cours[cours3].nom)

    def test_creer_etudiant(self):
        etudiant1 = ("Doe", "John", "123")
        etudiant2 = ("Smith", "Jane", "456")
        etudiant3 = ("Williams", "Pierre-Andre", "789")
        creer_etudiant(*etudiant1)
        creer_etudiant(*etudiant2)
        creer_etudiant(*etudiant3)
        self.assertEqual(etudiant1[2], dictionnaire_etudiants[etudiant1[2]].matricule)
        self.assertEqual(etudiant2[2], dictionnaire_etudiants[etudiant2[2]].matricule)
        self.assertEqual(etudiant3[2], dictionnaire_etudiants[etudiant3[2]].matricule)

    def test_attribuer_note(self):
        note1 = 12
        note2 = 16
        note3 = 20
        note4 = 18
        note5 = 10
        note6 = 16
        note7 = 15
        cours1 = "Anglais"
        cours2 = "Progra"
        cours3 = "Math"
        etudiant1 = ("Doe", "John", "123")
        etudiant2 = ("Smith", "Jane", "456")
        etudiant3 = ("Williams", "Bob", "789")

        attribuer_note(note1, etudiant1[2], cours1)
        attribuer_note(note2, etudiant1[2], cours2)
        attribuer_note(note3, etudiant1[2], cours3)
        attribuer_note(note4, etudiant2[2], cours1)
        attribuer_note(note5, etudiant2[2], cours2)
        attribuer_note(note6, etudiant2[2], cours3)
        attribuer_note(note7, etudiant3[2], cours1)
        attribuer_note(note4, etudiant3[2], cours2)
        attribuer_note(note1, etudiant3[2], cours3)

        self.assertEqual(note1, dictionnaire_cours[cours1].notes[etudiant1[2]])
        self.assertEqual(note2, dictionnaire_cours[cours2].notes[etudiant1[2]])
        self.assertEqual(note3, dictionnaire_cours[cours3].notes[etudiant1[2]])
        self.assertEqual(note4, dictionnaire_cours[cours1].notes[etudiant2[2]])
        self.assertEqual(note5, dictionnaire_cours[cours2].notes[etudiant2[2]])
        self.assertEqual(note6, dictionnaire_cours[cours3].notes[etudiant2[2]])
        self.assertEqual(note7, dictionnaire_cours[cours1].notes[etudiant3[2]])
        self.assertEqual(note4, dictionnaire_cours[cours2].notes[etudiant3[2]])
        self.assertEqual(note1, dictionnaire_cours[cours3].notes[etudiant3[2]])

    def test_trier_note(self):
            cours1 = "Math"
            cours2 = "Progra"
            cours3 = "Math"
            tri_notes = trier_notes()
            self.assertIsInstance(tri_notes, dict)
            self.assertTrue(cours1 in tri_notes)
            self.assertTrue(cours2 in tri_notes)
            self.assertTrue(cours3 in tri_notes)

    def test_afficher_note_triees(self):
        affichage_notes = afficher_notes_triees()
        self.assertIsNone(affichage_notes)

if __name__ == '__main__':
    unittest.main()
