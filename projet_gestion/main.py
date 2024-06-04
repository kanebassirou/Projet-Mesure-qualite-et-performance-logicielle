from datetime import datetime
from models.projet import Projet
from models.membre import Membre
from models.tache import Tache
from models.risque import Risque
from models.jalon import Jalon
from notifications.strategie_notification import (
    StrategieNotificationEmail,
    StrategieNotificationSMS,
    StrategieNotificationPush,
)


def saisir_membre():
    nom = input("Entrez le nom du membre: ")
    role = input("Entrez le rôle du membre: ")
    return Membre(nom, role)


def saisir_tache(membres):
    nom = input("Entrez le nom de la tâche: ")
    description = input("Entrez la description de la tâche: ")
    date_debut = datetime.strptime(
        input("Entrez la date de début (AAAA-MM-JJ): "), "%Y-%m-%d"
    )
    date_fin = datetime.strptime(
        input("Entrez la date de fin (AAAA-MM-JJ): "), "%Y-%m-%d"
    )
    print("Liste des membres disponibles:")
    for idx, membre in enumerate(membres):
        print(f"{idx}. {membre.nom} ({membre.role})")
    responsable_nom = input("Entrez le nom du responsable: ")
    responsable = None
    for membre in membres:
        if membre.nom == responsable_nom:
            responsable = membre
            break
    if responsable is None:
        print("Membre responsable non trouvé.")
        return
    statut = input("Entrez le statut de la tâche: ")
    return Tache(nom, description, date_debut, date_fin, responsable, statut)


def saisir_risque():
    description = input("Entrez la description du risque: ")
    probabilite = float(input("Entrez la probabilité du risque (0-1): "))
    impact = input("Entrez l'impact du risque: ")
    return Risque(description, probabilite, impact)


def saisir_jalon():
    nom = input("Entrez le nom du jalon: ")
    date = datetime.strptime(
        input("Entrez la date du jalon (AAAA-MM-JJ): "), "%Y-%m-%d"
    )
    return Jalon(nom, date)


def ajouter_membres(projet):
    membres = []
    while True:
        membre = saisir_membre()
        projet.ajouter_membre_equipe(membre)
        membres.append(membre)
        continuer = (
            input("Voulez-vous ajouter un autre membre? (oui/non): ").strip().lower()
        )
        if continuer != "oui":
            break
    return membres


def ajouter_taches(projet, membres):
    while True:
        tache = saisir_tache(membres)
        projet.ajouter_tache(tache)
        projet.notifier(f"Nouvelle tâche ajoutée: {tache.nom}", membres)
        continuer = (
            input("Voulez-vous ajouter une autre tâche? (oui/non): ").strip().lower()
        )
        if continuer != "oui":
            break


def ajouter_risques(projet):
    while True:
        risque = saisir_risque()
        projet.ajouter_risque(risque)
        continuer = (
            input("Voulez-vous ajouter un autre risque? (oui/non): ").strip().lower()
        )
        if continuer != "oui":
            break


def ajouter_jalons(projet):
    while True:
        jalon = saisir_jalon()
        projet.ajouter_jalon(jalon)
        continuer = (
            input("Voulez-vous ajouter un autre jalon? (oui/non): ").strip().lower()
        )
        if continuer != "oui":
            break


def main():
    nom_projet = input("Entrez le nom du projet: ")
    description_projet = input("Entrez la description du projet: ")
    date_debut_projet = datetime.strptime(
        input("Entrez la date de début du projet (AAAA-MM-JJ): "), "%Y-%m-%d"
    )
    date_fin_projet = datetime.strptime(
        input("Entrez la date de fin du projet (AAAA-MM-JJ): "), "%Y-%m-%d"
    )
    projet = Projet(nom_projet, description_projet, date_debut_projet, date_fin_projet)

    budget_projet = float(input("Entrez le montant du budget du projet: "))
    projet.definir_budget(budget_projet)

    choix_strategie = (
        input("Choisissez la stratégie de notification (email, sms, push): ")
        .strip()
        .lower()
    )
    if choix_strategie == "email":
        projet.definir_strategie_notification(StrategieNotificationEmail())
    elif choix_strategie == "sms":
        projet.definir_strategie_notification(StrategieNotificationSMS())
    elif choix_strategie == "push":
        projet.definir_strategie_notification(StrategieNotificationPush())
    else:
        print(
            "Stratégie de notification non reconnue, utilisation de la stratégie email par défaut."
        )
        projet.definir_strategie_notification(StrategieNotificationEmail())

    membres = ajouter_membres(projet)
    ajouter_taches(projet, membres)
    ajouter_risques(projet)
    ajouter_jalons(projet)

    changement = input("Entrez la description du changement: ")
    projet.enregistrer_changement(changement)

    rapport = projet.generer_rapport_performance()
    print(rapport)


if __name__ == "__main__":
    main()
