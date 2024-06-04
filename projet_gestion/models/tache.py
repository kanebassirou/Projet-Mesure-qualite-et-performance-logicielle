from datetime import datetime
from typing import List
from models.membre import Membre


class Tache:
    def __init__(
        self,
        nom: str,
        description: str,
        date_debut: datetime,
        date_fin: datetime,
        responsable: Membre,
        statut: str,
    ):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsable = responsable
        self.statut = statut
        self.dependances: List[Tache] = []
        self.duree = (date_fin - date_debut).days  # Calcul de la durée en jours

    def ajouter_dependance(self, tache):
        self.dependances.append(tache)

    def mettre_a_jour_statut(self, statut: str) -> None:
        self.statut = statut
