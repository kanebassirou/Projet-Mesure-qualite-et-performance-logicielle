"""
Module de gestion des stratégies de notification.

Ce module contient la classe abstraite StrategieNotification ainsi que ses sous-classes
pour envoyer des notifications à des destinataires.
"""

from typing import Any

class StrategieNotification:
    """
    Classe abstraite représentant une stratégie de notification.

    Methods:
        envoyer(message: str, destinataire: Any) -> None: Méthode 
        abstraite pour envoyer une notification.
    """

    def envoyer(self, message: str, destinataire: Any) -> None:
        """
        Envoyer une notification à un destinataire spécifié.

        Args:
            message (str): Le message à envoyer.
            destinataire (Any): Le destinataire de la notification.
        """
        raise NotImplementedError(
            "Cette méthode doit être surchargée dans une sous-classe"
        )


class StrategieNotificationEmail(StrategieNotification):
    """
    Stratégie de notification par email.

    Inherits:
        StrategieNotification: Classe abstraite représentant une stratégie de notification.

    Methods:
        envoyer(message: str, destinataire: Any) -> None: Envoyer une notification par email.
    """

    def envoyer(self, message: str, destinataire: Any) -> None:
        """
        Envoyer une notification par email à un destinataire spécifié.

        Args:
            message (str): Le message à envoyer.
            destinataire (Any): Le destinataire de la notification.
        """
        print(f"Notification envoyée à {destinataire.nom} par email: {message}")


class StrategieNotificationSMS(StrategieNotification):
    """
    Stratégie de notification par SMS.

    Inherits:
        StrategieNotification: Classe abstraite représentant une stratégie de notification.

    Methods:
        envoyer(message: str, destinataire: Any) -> None: Envoyer une notification par SMS.
    """

    def envoyer(self, message: str, destinataire: Any) -> None:
        """
        Envoyer une notification par SMS à un destinataire spécifié.

        Args:
            message (str): Le message à envoyer.
            destinataire (Any): Le destinataire de la notification.
        """
        print(f"Notification envoyée à {destinataire.nom} par SMS: {message}")


class StrategieNotificationPush(StrategieNotification):
    """
    Stratégie de notification par notification push.

    Inherits:
        StrategieNotification: Classe abstraite représentant une stratégie de notification.

    Methods:
        envoyer(message: str, destinataire: Any) -> None: Envoyer une notification par 
        notification push.
    """

    def envoyer(self, message: str, destinataire: Any) -> None:
        """
        Envoyer une notification par notification push à un destinataire spécifié.

        Args:
            message (str): Le message à envoyer.
            destinataire (Any): Le destinataire de la notification.
        """
        print(
            f"Notification envoyée à {destinataire.nom} par notification push: {message}"
        )
