"""
Module de gestion des projets.

Ce module contient la classe Projet qui permet de gérer un projet avec ses tâches,
son équipe, son budget, ses risques, ses jalons, et ses changements.
"""

from datetime import datetime, timedelta
from typing import List
from models.equipe import Equipe
from models.jalon import Jalon
from models.changement import Changement
from models.risque import Risque
from models.tache import Tache
from notifications.strategie_notification import StrategieNotification
from notifications.contexte_notification import ContexteNotification
from models.membre import Membre

class Projet:
    """
    Représente un projet avec ses différentes composantes.

    Attributs:
        nom (str): Le nom du projet.
        description (str): La description du projet.
        date_debut (datetime): La date de début du projet.
        date_fin (datetime): La date de fin du projet.
        taches (List[Tache]): La liste des tâches du projet.
        equipe (Equipe): L'équipe du projet.
        budget (float): Le budget du projet.
        risques (List[Risque]): La liste des risques du projet.
        jalons (List[Jalon]): La liste des jalons du projet.
        version (int): La version actuelle du projet.
        changements (List[Changement]): La liste des changements du projet.
        chemin_critique (List[Tache]): La liste des tâches du chemin critique du projet.
        contexte_notification (ContexteNotification): Le contexte de notification du projet.
    """

    def __init__(
        self, nom: str, description: str, date_debut: datetime, date_fin: datetime
    ):
        """
        Initialise une nouvelle instance de la classe Projet.

        Args:
            nom (str): Le nom du projet.
            description (str): La description du projet.
            date_debut (datetime): La date de début du projet.
            date_fin (datetime): La date de fin du projet.
        """
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.taches: List[Tache] = []
        self.equipe = Equipe()
        self.budget = 0.0
        self.risques: List[Risque] = []
        self.jalons: List[Jalon] = []
        self.version = 1
        self.changements: List[Changement] = []
        self.chemin_critique: List[Tache] = []
        self.contexte_notification = None

    def definir_strategie_notification(self, strategie: StrategieNotification) -> None:
        """
        Définit la stratégie de notification pour le projet.

        Args:
            strategie (StrategieNotification): La stratégie de notification à appliquer.
        """
        self.contexte_notification = ContexteNotification(strategie)

    def ajouter_tache(self, tache: Tache) -> None:
        """
        Ajoute une tâche au projet.

        Args:
            tache (Tache): La tâche à ajouter au projet.
        """
        self.taches.append(tache)

    def ajouter_membre_equipe(self, membre: Membre) -> None:
        """
        Ajoute un membre à l'équipe du projet.

        Args:
            membre (Membre): Le membre à ajouter à l'équipe.
        """
        self.equipe.ajouter_membre(membre)
        self.notifier(f"{membre.nom} a été ajouté à l'équipe", [membre])

    def definir_budget(self, budget: float) -> None:
        """
        Définit le budget du projet.

        Args:
            budget (float): Le budget à allouer au projet.
        """
        self.budget = budget
        self.notifier(
            f"Le budget du projet a été défini à {budget} Unité Monetaire",
            self.equipe.obtenir_membres(),
        )

    def ajouter_risque(self, risque: Risque) -> None:
        """
        Ajoute un risque au projet.

        Args:
            risque (Risque): Le risque à ajouter au projet.
        """
        self.risques.append(risque)
        self.notifier(
            f"Nouveau risque ajouté: {risque.description}",
            self.equipe.obtenir_membres(),
        )

    def ajouter_jalon(self, jalon: Jalon) -> None:
        """
        Ajoute un jalon au projet.

        Args:
            jalon (Jalon): Le jalon à ajouter au projet.
        """
        self.jalons.append(jalon)
        self.notifier(
            f"Nouveau jalon ajouté: {jalon.nom}", self.equipe.obtenir_membres()
        )

    def enregistrer_changement(self, description: str) -> None:
        """
        Enregistre un changement pour le projet.

        Args:
            description (str): La description du changement.
        """
        changement = Changement(description, self.version, datetime.now())
        self.changements.append(changement)
        self.version += 1
        self.notifier(
            f"Changement enregistré: {description} (version {self.version})",
            self.equipe.obtenir_membres(),
        )

    def generer_rapport_performance(self) -> str:
        """
        Génère un rapport de performance pour le projet.

        Returns:
            str: Un rapport de performance détaillé du projet.
        """
        rapport = f"Rapport de performance pour le projet: {self.nom}\n"
        rapport += f"Description: {self.description}\n"
        rapport += f"Dates: {self.date_debut} - {self.date_fin}\n"
        rapport += f"Budget: {self.budget} Unité Monetaire\n\n"

        rapport += "Équipe:\n"
        for membre in self.equipe.obtenir_membres():
            rapport += f" - {membre.nom} ({membre.role})\n"

        rapport += "\nTâches:\n"
        for tache in self.taches:
            rapport += (
                f" - {tache.nom}: {tache.description} (Responsable: {tache.responsable.nom}, "
                f"Statut: {tache.statut}, Début: {tache.date_debut}, Fin: {tache.date_fin})\n"
            )

        rapport += "\nJalons:\n"
        for jalon in self.jalons:
            rapport += f" - {jalon.nom} (Date: {jalon.date})\n"

        rapport += "\nRisques:\n"
        for risque in self.risques:
            rapport += f" - {risque.description} (\n" \
                       f"  Probabilité: {risque.probabilite}, \n" \
                       f"  Impact: {risque.impact})\n"
        rapport += "\nChangements:\n"
        for changement in self.changements:
            rapport += f"- {changement.description} (\n" \
                       f"Version: {changement.version}, \n"\
                       f"Date: {changement.date})\n"
        rapport += "\nChemin Critique:\n"
        chemin_critique = self.calculer_chemin_critique()
        for tache in chemin_critique:
            rapport += f"- {tache.nom} ({tache.date_debut.strftime('%Y-%m-%d')}" \
                    f"à {tache.date_fin.strftime('%Y-%m-%d')})\n"
        return rapport

    def calculer_chemin_critique(self) -> List[Tache]:
        """
        Calcule et retourne le chemin critique du projet.

        Returns:
            List[Tache]: La liste des tâches formant le chemin critique.
        """
        # Assurez-vous que les dates de début et de fin sont calculées correctement.
        for tache in self.taches:
            tache.fin_tot = tache.date_debut + timedelta(
                days=(tache.date_fin - tache.date_debut).days
            )
            tache.debut_tot = tache.date_debut

        # Calcul du chemin critique
        chemin_critique = []
        for tache in self.taches:
            if tache.dependances:
                max_fin = max(dep.fin_tot for dep in tache.dependances)
                tache.debut_tot = max_fin
                tache.fin_tot = tache.debut_tot + timedelta(
                    days=(tache.date_fin - tache.date_debut).days
                )

        # Trouver les tâches qui font partie du chemin critique
        max_fin = max(t.fin_tot for t in self.taches)
        for tache in self.taches:
            if tache.fin_tot == max_fin:
                chemin_critique.append(tache)
                while tache.dependances:
                    tache = max(tache.dependances, key=lambda t: t.fin_tot)
                    chemin_critique.append(tache)
                break

        return list(reversed(chemin_critique))

    def notifier(self, message: str, destinataires: List[Membre]) -> None:
        """
        Envoie une notification avec un message spécifique à une liste de destinataires.

        Args:
            message (str): Le message à envoyer.
            destinataires (List[Membre]): La liste des membres à notifier.
        """
        if self.contexte_notification:
            self.contexte_notification.notifier(message, destinataires)
