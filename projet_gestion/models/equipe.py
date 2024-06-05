"""
Module de gestion des équipes.

Ce module contient la classe Equipe qui permet de gérer une équipe de membres.
"""

from typing import List
from models.membre import Membre

class Equipe:
    """
    Représente une équipe composée de membres.

    Attributs:
        membres (List[Membre]): La liste des membres de l'équipe.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance de la classe Equipe.
        """
        self.membres = []

    def ajouter_membre(self, membre: Membre) -> None:
        """
        Ajoute un membre à l'équipe.

        Args:
            membre (Membre): Le membre à ajouter à l'équipe.
        """
        self.membres.append(membre)

    def obtenir_membres(self) -> List[Membre]:
        """
        Retourne la liste des membres de l'équipe.

        Returns:
            List[Membre]: La liste des membres de l'équipe.
        """
        return self.membres
