import unittest
from datetime import datetime
from models.projet import Projet
from models.membre import Membre
from models.tache import Tache
from models.risque import Risque
from models.jalon import Jalon
from notifications.strategie_notification import StrategieNotificationEmail

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
        
    def test_generer_rapport_performance(self):
        # Ajout des tâches nécessaires pour générer le rapport
        tache1 = Tache("Tâche 1", "Description Tâche 1", datetime(2024, 1, 1), datetime(2024, 2, 1), self.membre, "En cours")
        tache2 = Tache("Tâche 2", "Description Tâche 2", datetime(2024, 2, 2), datetime(2024, 3, 1), self.membre, "En cours")
        tache3 = Tache("Tâche 3", "Description Tâche 3", datetime(2024, 3, 2), datetime(2024, 4, 1), self.membre, "En cours")
        tache2.ajouter_dependance(tache1)
        tache3.ajouter_dependance(tache2)

        self.projet.ajouter_tache(tache1)
        self.projet.ajouter_tache(tache2)
        self.projet.ajouter_tache(tache3)

        rapport = self.projet.generer_rapport_performance()
        self.assertIsInstance(rapport, str)  # Vérifie que le rapport est une chaîne de caractères

    def test_calculer_chemin_critique(self):
        tache1 = Tache("Tâche 1", "Description Tâche 1", datetime(2024, 1, 1), datetime(2024, 2, 1), self.membre, "En cours")
        tache2 = Tache("Tâche 2", "Description Tâche 2", datetime(2024, 2, 2), datetime(2024, 3, 1), self.membre, "En cours")
        tache3 = Tache("Tâche 3", "Description Tâche 3", datetime(2024, 3, 2), datetime(2024, 4, 1), self.membre, "En cours")
        tache2.ajouter_dependance(tache1)
        tache3.ajouter_dependance(tache2)

        self.projet.ajouter_tache(tache1)
        self.projet.ajouter_tache(tache2)
        self.projet.ajouter_tache(tache3)

        chemin_critique = self.projet.calculer_chemin_critique()

        # Afficher les tâches pour débogage
        for tache in chemin_critique:
            print(f"Tâche: {tache.nom}, Début: {tache.date_debut}, Fin: {tache.date_fin}")

        # Comparer les attributs des tâches
        chemin_critique_attendu = [(tache1.nom, tache1.date_debut, tache1.date_fin),
                                   (tache2.nom, tache2.date_debut, tache2.date_fin),
                                   (tache3.nom, tache3.date_debut, tache3.date_fin)]

        chemin_critique_calcule = [(tache.nom, tache.date_debut, tache.date_fin) for tache in chemin_critique]

        self.assertEqual(chemin_critique_calcule, chemin_critique_attendu)

if __name__ == "__main__":
    unittest.main()
