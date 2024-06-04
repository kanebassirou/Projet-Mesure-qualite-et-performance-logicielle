import unittest
from io import StringIO
from contextlib import redirect_stdout
from datetime import datetime
from unittest.mock import patch

from models.projet import Projet
from models.membre import Membre
from models.tache import Tache
from models.risque import Risque
from models.jalon import Jalon
from notifications.strategie_notification import (
    StrategieNotificationEmail,
    StrategieNotificationSMS,
    StrategieNotificationPush,
)


class TestProjet(unittest.TestCase):

    def setUp(self):
        self.projet = Projet(
            "Projet Test",
            "Description Test",
            datetime(2024, 1, 1),
            datetime(2024, 12, 31),
        )
        self.membre = Membre("bassirou kane", "Développeur")
        self.responsable = Membre("bassirou kane", "Développeur")
        self.tache = Tache(
            "Tâche Test",
            "Description Tâche",
            datetime(2024, 1, 1),
            datetime(2024, 6, 30),
            self.membre,
            "En cours",
        )
        self.risque = Risque("Risque Test", 0.5, "Moyen")
        self.jalon = Jalon("Jalon Test", datetime(2024, 6, 30))
        self.projet.definir_strategie_notification(StrategieNotificationEmail())
        self.message = "Vous avez une nouvelle notification"

    def test_notifier(self):
        destinataires = [self.membre]
        message = "Test de notification"
        with patch.object(self.projet.contexte_notification, "notifier") as mock_notif:
            self.projet.notifier(message, destinataires)
            mock_notif.assert_called_once_with(message, destinataires)

    def test_strategie_notification_email(self):
        strategie = StrategieNotificationEmail()
        with StringIO() as buf, redirect_stdout(buf):
            strategie.envoyer(self.message, self.membre)
            output = buf.getvalue()
        self.assertIn(
            f"Notification envoyée à {self.membre.nom} par email: {self.message}",
            output,
        )

    def test_strategie_notification_sms(self):
        strategie = StrategieNotificationSMS()
        with StringIO() as buf, redirect_stdout(buf):
            strategie.envoyer(self.message, self.membre)
            output = buf.getvalue()
        self.assertIn(
            f"Notification envoyée à {self.membre.nom} par SMS: {self.message}", output
        )

    def test_strategie_notification_push(self):
        strategie = StrategieNotificationPush()
        with StringIO() as buf, redirect_stdout(buf):
            strategie.envoyer(self.message, self.membre)
            output = buf.getvalue()
        self.assertIn(
            f"Notification envoyée à {self.membre.nom} par notification push: {self.message}",
            output,
        )

    def test_ajouter_membre_equipe(self):
        # Vérification avant l'ajout
        self.assertNotIn(self.membre, self.projet.equipe.obtenir_membres())
        # Ajout du membre
        self.projet.ajouter_membre_equipe(self.membre)
        # Vérification après l'ajout
        self.assertIn(self.membre, self.projet.equipe.obtenir_membres())

    def test_ajouter_tache(self):
        # Vérification avant l'ajout
        self.assertNotIn(self.tache, self.projet.taches)
        # Ajout de la tâche
        self.projet.ajouter_tache(self.tache)
        # Vérification après l'ajout
        self.assertIn(self.tache, self.projet.taches)

    def test_ajouter_risque(self):
        # Vérification avant l'ajout
        self.assertNotIn(self.risque, self.projet.risques)
        # Ajout du risque
        self.projet.ajouter_risque(self.risque)
        # Vérification après l'ajout
        self.assertIn(self.risque, self.projet.risques)

    def test_ajouter_jalon(self):
        # Vérification avant l'ajout
        self.assertNotIn(self.jalon, self.projet.jalons)
        # Ajout du jalon
        self.projet.ajouter_jalon(self.jalon)
        # Vérification après l'ajout
        self.assertIn(self.jalon, self.projet.jalons)

    def test_enregistrer_changement(self):
        self.projet.enregistrer_changement("Description Changement")
        dernier_changement = self.projet.changements[-1]
        self.assertEqual(dernier_changement.description, "Description Changement")
        self.assertEqual(dernier_changement.version, 1)

    def test_generer_rapport_performance(self):
        # Ajout des tâches nécessaires pour générer le rapport
        tache1 = Tache(
            "Tâche 1",
            "Description Tâche 1",
            datetime(2024, 1, 1),
            datetime(2024, 2, 1),
            self.membre,
            "En cours",
        )
        tache2 = Tache(
            "Tâche 2",
            "Description Tâche 2",
            datetime(2024, 2, 2),
            datetime(2024, 3, 1),
            self.membre,
            "En cours",
        )
        tache3 = Tache(
            "Tâche 3",
            "Description Tâche 3",
            datetime(2024, 3, 2),
            datetime(2024, 4, 1),
            self.membre,
            "En cours",
        )
        tache2.ajouter_dependance(tache1)
        tache3.ajouter_dependance(tache2)

        self.projet.ajouter_tache(tache1)
        self.projet.ajouter_tache(tache2)
        self.projet.ajouter_tache(tache3)

        rapport = self.projet.generer_rapport_performance()
        self.assertIsInstance(
            rapport, str
        )  # Vérifie que le rapport est une chaîne de caractères
        self.assertIn("Rapport de performance pour le projet: Projet Test", rapport)

    def test_calculer_chemin_critique(self):
        # Création des tâches avec des dépendances
        tache1 = Tache(
            "Tâche 1",
            "Description Tâche 1",
            datetime(2024, 1, 1),
            datetime(2024, 2, 1),
            self.responsable,
            "En cours",
        )
        tache2 = Tache(
            "Tâche 2",
            "Description Tâche 2",
            datetime(2024, 2, 2),
            datetime(2024, 3, 1),
            self.responsable,
            "En cours",
        )
        tache3 = Tache(
            "Tâche 3",
            "Description Tâche 3",
            datetime(2024, 3, 2),
            datetime(2024, 4, 1),
            self.responsable,
            "En cours",
        )
        tache2.ajouter_dependance(tache1)
        tache3.ajouter_dependance(tache2)

        # Ajout des tâches au projet
        self.projet.ajouter_tache(tache1)
        self.projet.ajouter_tache(tache2)
        self.projet.ajouter_tache(tache3)

        # Exécution de la méthode à tester
        chemin_critique = self.projet.calculer_chemin_critique()

        # Vérification des résultats
        self.assertIsInstance(chemin_critique, list)
        self.assertEqual(
            chemin_critique, [tache1, tache2, tache3]
        )  # Vérifie que les tâches sont dans le bon ordre

    def test_definir_budget(self):
        budget = 100000.0
        self.projet.definir_budget(budget)
        self.assertEqual(self.projet.budget, budget)

    def test_notification_definir_budget(self):
        with patch.object(self.projet.contexte_notification, "notifier") as mock_notif:
            budget = 100000.0
            self.projet.definir_budget(budget)
            mock_notif.assert_called_once_with(
                f"Le budget du projet a été défini à {budget} Unité Monetaire",
                self.projet.equipe.obtenir_membres(),
            )

    def test_notification_ajouter_membre_equipe(self):
        with patch.object(self.projet.contexte_notification, "notifier") as mock_notif:
            self.projet.ajouter_membre_equipe(self.membre)
            mock_notif.assert_called_once_with(
                f"{self.membre.nom} a été ajouté à l'équipe", [self.membre]
            )


if __name__ == "__main__":
    unittest.main()
