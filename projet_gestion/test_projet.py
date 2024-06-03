import unittest
from datetime import datetime
from models.projet import Projet
from  models.membre import Membre
from  models.tache import Tache
from  models.risque import Risque
from  models.jalon import Jalon
from  models.changement import Changement
from  notifications.strategie_notification import StrategieNotificationEmail

class TestProjet(unittest.TestCase):

    def setUp(self):
        self.projet = Projet("Projet Test", "Description Test", datetime(2024, 1, 1), datetime(2024, 12, 31))
        self.membre = Membre("John Doe", "Développeur")
        self.tache = Tache("Tâche Test", "Description Tâche", datetime(2024, 1, 1), datetime(2024, 6, 30), self.membre, "En cours")
        self.risque = Risque("Risque Test", 0.5, "Moyen")
        self.jalon = Jalon("Jalon Test", datetime(2024, 6, 30))
        self.projet.definir_strategie_notification(StrategieNotificationEmail())

    def test_ajouter_membre_equipe(self):
        self.projet.ajouter_membre_equipe(self.membre)
        self.assertIn(self.membre, self.projet.equipe.obtenir_membres())

    def test_ajouter_tache(self):
        self.projet.ajouter_tache(self.tache)
        self.assertIn(self.tache, self.projet.taches)

    def test_ajouter_risque(self):
        self.projet.ajouter_risque(self.risque)
        self.assertIn(self.risque, self.projet.risques)

    def test_ajouter_jalon(self):
        self.projet.ajouter_jalon(self.jalon)
        self.assertIn(self.jalon, self.projet.jalons)

    def test_enregistrer_changement(self):
        self.projet.enregistrer_changement("Description Changement")
        self.assertEqual(len(self.projet.changements), 1)

if __name__ == "__main__":
    unittest.main()
