"""
Module de gestion des tâches.

Ce module contient la classe Tache qui représente une tâche avec un nom,
une description, des dates de début et de fin, un responsable, un statut, et des dépendances.
"""

from datetime import datetime
from typing import List
from models.membre import Membre


class Tache:
    """
    Représente une tâche avec un nom, une description, des dates de début 
    et de fin, un responsable, un statut, et des dépendances.

    Attributs:
        nom (str): Le nom de la tâche.
        description (str): La description de la tâche.
        date_debut (datetime): La date de début de la tâche.
        date_fin (datetime): La date de fin de la tâche.
        responsable (Membre): Le membre responsable de la tâche.
        statut (str): Le statut de la tâche.
        dependances (List[Tache]): La liste des tâches dont dépend cette tâche.
        duree (int): La durée de la tâche en jours.
    """

    def __init__(
        self,
        nom: str,
        description: str,
        date_debut: datetime,
        date_fin: datetime,
        responsable: Membre,
        statut: str,
    ):
        """
        Initialise une nouvelle instance de la classe Tache.

        Args:
            nom (str): Le nom de la tâche.
            description (str): La description de la tâche.
            date_debut (datetime): La date de début de la tâche.
            date_fin (datetime): La date de fin de la tâche.
            responsable (Membre): Le membre responsable de la tâche.
            statut (str): Le statut de la tâche.
        """
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsable = responsable
        self.statut = statut
        self.dependances: List[Tache] = []
        self.duree = (date_fin - date_debut).days  # Calcul de la durée en jours

    def ajouter_dependance(self, tache: 'Tache') -> None:
        """
        Ajoute une tâche dont dépend cette tâche.

        Args:
            tache (Tache): La tâche dont dépend cette tâche.
        """
        self.dependances.append(tache)

    def mettre_a_jour_statut(self, statut: str) -> None:
        """
        Met à jour le statut de la tâche.

        Args:
            statut (str): Le nouveau statut de la tâche.
        """
        self.statut = statut
