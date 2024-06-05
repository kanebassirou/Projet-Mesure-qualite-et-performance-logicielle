"""
Module de gestion des notifications.

Ce module contient la classe ContexteNotification, qui représente 
le contexte pour l'envoi de notifications
à des membres d'une équipe de projet.
"""

from typing import List
from notifications.strategie_notification import StrategieNotification
from models.membre import Membre

class ContexteNotification:
    """
    Contexte de notification pour l'envoi de messages aux membres.

    Attributes:
        strategie (StrategieNotification): La stratégie de notification à utiliser.
    """

    def __init__(self, strategie: StrategieNotification):
        """
        Initialise une nouvelle instance de ContexteNotification.

        Args:
            strategie (StrategieNotification): La stratégie de notification à utiliser.
        """
        self.strategie = strategie

    def notifier(self, message: str, destinataires: List[Membre]) -> None:
        """
        Notifie les destinataires avec le message spécifié.

        Args:
            message (str): Le message à envoyer.
            destinataires (List[Membre]): La liste des membres à notifier.
        """
        for destinataire in destinataires:
            self.strategie.envoyer(message, destinataire)
