class StrategieNotification:
    def envoyer(self, message: str, destinataire: 'Membre') -> None:
        raise NotImplementedError("Cette méthode doit être surchargée dans une sous-classe")

class StrategieNotificationEmail(StrategieNotification):
    def envoyer(self, message: str, destinataire: 'Membre') -> None:
        print(f"Notification envoyée à {destinataire.nom} par email: {message}")

class StrategieNotificationSMS(StrategieNotification):
    def envoyer(self, message: str, destinataire: 'Membre') -> None:
        print(f"Notification envoyée à {destinataire.nom} par SMS: {message}")

class StrategieNotificationPush(StrategieNotification):
    def envoyer(self, message: str, destinataire: 'Membre') -> None:
        print(f"Notification envoyée à {destinataire.nom} par notification push: {message}")
