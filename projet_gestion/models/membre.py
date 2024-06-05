"""
Module de gestion des membre.

Ce module contient la classe memebre qui représente un membre son nom et role
dans projet.
"""
class Membre:
    """
    Represents a member.
    """

    def __init__(self, nom: str, role: str):
        """
        Initializes a new instance of the Membre class.

        Args:
            nom (str): The name of the member.
            role (str): The role of the member.
        """
        self.nom = nom
        self.role = role
