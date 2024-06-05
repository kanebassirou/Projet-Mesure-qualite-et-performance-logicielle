"""
Module de gestion des changements de version.

Ce module contient la classe Changement qui représente un changement dans un système de versionnage.
"""

from datetime import datetime

class Changement:
    """
    Représente un changement dans un système de versionnage.

    Attributs:
        description (str): La description du changement.
        version (int): La version associée au changement.
        date (datetime): La date du changement.
    """

    def __init__(self, description: str, version: int, date: datetime):
        """
        Initialise une nouvelle instance de la classe Changement.

        Args:
            description (str): La description du changement.
            version (int): La version associée au changement.
            date (datetime): La date du changement.
        """
        self.description = description
        self.version = version
        self.date = date

    def get_details(self) -> str:
        """
        Retourne les détails du changement sous forme de chaîne de caractères.

        Returns:
            str: Une chaîne de caractères contenant les détails du changement.
        """
        return (
            f"Version {self.version}: {self.description} "
            f"(Date: {self.date.strftime('%Y-%m-%d')})"
        )

    def is_recent(self, days: int) -> bool:
        """
        Détermine si le changement est récent par rapport au nombre de jours spécifié.

        Args:
            days (int): Le nombre de jours pour définir la récence.

        Returns:
            bool: True si le changement est récent, False sinon.
        """
        delta = datetime.now() - self.date
        return delta.days <= days
