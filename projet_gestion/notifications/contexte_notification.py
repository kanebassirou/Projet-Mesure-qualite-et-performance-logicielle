from typing import List
from notifications.strategie_notification import StrategieNotification
from models.membre import Membre

class ContexteNotification:
    def __init__(self, strategie: StrategieNotification):
        self.strategie = strategie

    def notifier(self, message: str, destinataires: List[Membre]) -> None:
        for destinataire in destinataires:
            self.strategie.envoyer(message, destinataire)
