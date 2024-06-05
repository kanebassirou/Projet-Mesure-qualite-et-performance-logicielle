"""
Ce module contient la fonctionnalité principale pour la
gestion d'un projet. Il comprend des fonctions pour capturer
les détails du projet, ajouter des membres, des tâches,
des risques et des jalons au projet, définir une stratégie
de notification et générer un rapport de performance.
Le module utilise différents modèles tels que `Projet`,
`Membre`, `Tache`, `Risque` et `Jalon` pour représenter
les différents aspects du projet.
Le module inclut également des stratégies de notification
telles que `StrategieNotificationEmail`, `StrategieNotificationSMS`
et `StrategieNotificationPush` pour envoyer des notifications aux
membres du projet.
Pour utiliser ce module, exécutez la fonction `main()`.
Remarque : Ce module suppose que les modèles nécessaires
et les stratégies de notification sont importés à partir de
leurs modules respectifs.
"""

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
    """
    Saisit les informations d'un membre.

    Returns:
        Membre: L'objet Membre créé avec les informations saisies.
    """
    nom = input("Entrez le nom du membre: ")
    role = input("Entrez le rôle du membre: ")
    return Membre(nom, role)


def saisir_tache(membres):
    """
    Saisit les informations d'une tâche.

    Args:
        membres (list): La liste des membres disponibles.

    Returns:
        Tache: L'objet Tache créé avec les informations saisies.
    """
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
        return None
    statut = input("Entrez le statut de la tâche: ")
    return Tache(nom, description, date_debut, date_fin, responsable, statut)


def saisir_risque():
    """
    Saisit les informations d'un risque.

    Returns:
        Risque: L'objet Risque créé avec les informations saisies.
    """
    description = input("Entrez la description du risque: ")
    probabilite = float(input("Entrez la probabilité du risque (0-1): "))
    impact = input("Entrez l'impact du risque: ")
    return Risque(description, probabilite, impact)


def saisir_jalon():
    """
    Saisit les informations d'un jalon.

    Returns:
        Jalon: L'objet Jalon créé avec les informations saisies.
    """
    nom = input("Entrez le nom du jalon: ")
    date = datetime.strptime(
        input("Entrez la date du jalon (AAAA-MM-JJ): "), "%Y-%m-%d"
    )
    return Jalon(nom, date)


def ajouter_membres(projet):
    """
    Ajoute des membres à l'équipe du projet.

    Args:
        projet (Projet): Le projet auquel ajouter les membres.

    Returns:
        list: La liste des membres ajoutés.
    """
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
    """
    Ajoute des tâches au projet.

    Args:
        projet (Projet): Le projet auquel ajouter les tâches.
        membres (list): La liste des membres disponibles.

    Returns:
        None
    """
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
    """
    Ajoute des risques au projet.

    Args:
        projet (Projet): Le projet auquel ajouter les risques.

    Returns:
        None
    """
    while True:
        risque = saisir_risque()
        projet.ajouter_risque(risque)
        continuer = (
            input("Voulez-vous ajouter un autre risque? (oui/non): ").strip().lower()
        )
        if continuer != "oui":
            break


def ajouter_jalons(projet):
    """
    Ajoute des jalons au projet.

    Args:
        projet (Projet): Le projet auquel ajouter les jalons.

    Returns:
        None
    """
    while True:
        jalon = saisir_jalon()
        projet.ajouter_jalon(jalon)
        continuer = (
            input("Voulez-vous ajouter un autre jalon? (oui/non): ").strip().lower()
        )
        if continuer != "oui":
            break


def main():
    """
    Cette fonction est le point d'entrée du programme.
    Elle demande à l'utilisateur de saisir des informations
    sur un projet,
    crée un objet `Projet` avec les informations fournies et
    effectue diverses opérations sur le projet.
    La fonction demande à l'utilisateur de saisir le nom du projet,
    la description, la date de début, la date de fin, le budget et
    la stratégie de notification. Elle crée ensuite un objet `Projet`
    avec les informations fournies et définit le budget et la stratégie
    de notification. Elle demande également à l'utilisateur d'ajouter
    des membres, des tâches, des risques et des jalons au projet.
    Enfin, elle demande à l'utilisateur de saisir une description
    d'un changement et de l'enregistrer dans le projet. Elle génère
    un rapport de performance pour le projet et l'affiche.

    Cette fonction ne prend aucun argument et ne renvoie aucune valeur.
    """
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
