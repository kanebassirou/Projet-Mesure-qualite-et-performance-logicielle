from datetime import datetime
from datetime import timedelta
from typing import List
from models.equipe import Equipe
from models.jalon import Jalon
from models.changement import Changement
from models.risque import Risque
from models.tache import Tache
from notifications.strategie_notification import StrategieNotification
from notifications.contexte_notification import ContexteNotification
from models.membre import Membre

class Projet:
    def __init__(self, nom: str, description: str, date_debut: datetime, date_fin: datetime):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.taches = []
        self.equipe = Equipe()
        self.budget = 0.0
        self.risques = []
        self.jalons = []
        self.version = 1
        self.changements = []
        self.chemin_critique = []
        self.contexte_notification = None

    def definir_strategie_notification(self, strategie: StrategieNotification) -> None:
        self.contexte_notification = ContexteNotification(strategie)

    def ajouter_tache(self, tache: Tache) -> None:
        self.taches.append(tache)

    def ajouter_membre_equipe(self, membre: Membre) -> None:
        self.equipe.ajouter_membre(membre)
        self.notifier(f"{membre.nom} a été ajouté à l'équipe", [membre])

    def definir_budget(self, budget: float) -> None:
        self.budget = budget
        self.notifier(f"Le budget du projet a été défini à {budget} Unité Monetaire", self.equipe.obtenir_membres())

    def ajouter_risque(self, risque: Risque) -> None:
        self.risques.append(risque)
        self.notifier(f"Nouveau risque ajouté: {risque.description}", self.equipe.obtenir_membres())

    def ajouter_jalon(self, jalon: Jalon) -> None:
        self.jalons.append(jalon)
        self.notifier(f"Nouveau jalon ajouté: {jalon.nom}", self.equipe.obtenir_membres())

    def enregistrer_changement(self, description: str) -> None:
        changement = Changement(description, self.version, datetime.now())
        self.changements.append(changement)
        self.version += 1
        self.notifier(f"Changement enregistré: {description} (version {self.version})", self.equipe.obtenir_membres())

    def generer_rapport_performance(self) -> str:
        rapport = f"Rapport de performance pour le projet: {self.nom}\n"
        rapport += f"Description: {self.description}\n"
        rapport += f"Dates: {self.date_debut} - {self.date_fin}\n"
        rapport += f"Budget: {self.budget} Unité Monetaire\n\n"
        
        rapport += "Équipe:\n"
        for membre in self.equipe.obtenir_membres():
            rapport += f" - {membre.nom} ({membre.role})\n"
        
        rapport += "\nTâches:\n"
        for tache in self.taches:
            rapport += f" - {tache.nom}: {tache.description} (Responsable: {tache.responsable.nom}, Statut: {tache.statut}, Début: {tache.date_debut}, Fin: {tache.date_fin})\n"
        
        rapport += "\nJalons:\n"
        for jalon in self.jalons:
            rapport += f" - {jalon.nom} (Date: {jalon.date})\n"
        
        rapport += "\nRisques:\n"
        for risque in self.risques:
            rapport += f" - {risque.description} (Probabilité: {risque.probabilite}, Impact: {risque.impact})\n"
        
        rapport += "\nChangements:\n"
        for changement in self.changements:
            rapport += f" - {changement.description} (Version: {changement.version}, Date: {changement.date})\n"
        
        rapport += "\nChemin Critique:\n"
        chemin_critique = self.calculer_chemin_critique()
        for tache in chemin_critique:
             rapport += f" - {tache.nom} ({tache.date_debut.strftime('%Y-%m-%d')} à {tache.date_fin.strftime('%Y-%m-%d')})\n"
    
        
        return rapport

    def calculer_chemin_critique(self):
        # Assurez-vous que les dates de début et de fin sont calculées correctement.
        for tache in self.taches:
            tache.fin_tot = tache.date_debut + timedelta(days=(tache.date_fin - tache.date_debut).days)
            tache.debut_tot = tache.date_debut

        chemin_critique = []
        for tache in self.taches:
            if tache.dependances:
                max_fin = max(dep.fin_tot for dep in tache.dependances)
                tache.debut_tot = max_fin
                tache.fin_tot = tache.debut_tot + timedelta(days=(tache.date_fin - tache.date_debut).days)
            if tache.fin_tot == max(t.fin_tot for t in self.taches):
                chemin_critique.append(tache)

        return chemin_critique

    def notifier(self, message: str, destinataires: List[Membre]) -> None:
        if self.contexte_notification:
            self.contexte_notification.notifier(message, destinataires)
