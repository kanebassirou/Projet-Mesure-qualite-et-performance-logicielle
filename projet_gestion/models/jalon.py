"""
Module de gestion des jalons.

Ce module contient la classe Jalon qui représente un jalon avec un nom et une date.
"""
from datetime import datetime
class Jalon:
    """
    Représente un jalon avec un nom et une date.

    Attributs:
        nom (str): Le nom du jalon.
        date (datetime): La date du jalon.
    """
    def __init__(self, nom: str, date: datetime):
        """
        Initialise une nouvelle instance de la classe Jalon.

        Args:
            nom (str): Le nom du jalon.
            date (datetime): La date du jalon.
        """
        self.nom = nom
        self.date = date   
