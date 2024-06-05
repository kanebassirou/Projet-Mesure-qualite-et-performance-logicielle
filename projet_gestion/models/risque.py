"""
Module de gestion des risques.

Ce module contient la classe Risque qui représente un risque avec une description,
une probabilité et un impact.
"""

class Risque:
    """
    Représente un risque avec une description, une probabilité et un impact.

    Attributs:
        description (str): La description du risque.
        probabilite (float): La probabilité du risque.
        impact (str): L'impact du risque.
    """

    def __init__(self, description: str, probabilite: float, impact: str):
        """
        Initialise une nouvelle instance de la classe Risque.

        Args:
            description (str): La description du risque.
            probabilite (float): La probabilité du risque.
            impact (str): L'impact du risque.
        """
        self.description = description
        self.probabilite = probabilite
        self.impact = impact
