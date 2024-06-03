from datetime import datetime
from models.membre import Membre
from models.tache import Tache
from models.risque import Risque
from models.jalon import Jalon

def saisir_membre() -> Membre:
    nom = input("Entrez le nom du membre: ")
    role = input("Entrez le rôle du membre: ")
    return Membre(nom, role)

def saisir_tache(membres: list) -> Tache:
    nom = input("Entrez le nom de la tâche: ")
    description = input("Entrez la description de la tâche: ")
    date_debut = datetime.strptime(input("Entrez la date de début (AAAA-MM-JJ): "), '%Y-%m-%d')
    date_fin = datetime.strptime(input("Entrez la date de fin (AAAA-MM-JJ): "), '%Y-%m-%d')
    print("Liste des membres disponibles pour la tâche:")
    for i, membre in enumerate(membres):
        print(f"{i+1}. {membre.nom} ({membre.role})")
    index_responsable = int(input("Sélectionnez le responsable (numéro): ")) - 1
    responsable = membres[index_responsable]
    statut = input("Entrez le statut de la tâche: ")
    return Tache(nom, description, date_debut, date_fin, responsable, statut)

def saisir_risque() -> Risque:
    description = input("Entrez la description du risque: ")
    probabilite = float(input("Entrez la probabilité du risque (0.0 - 1.0): "))
    impact = input("Entrez l'impact du risque: ")
    return Risque(description, probabilite, impact)

def saisir_jalon() -> Jalon:
    nom = input("Entrez le nom du jalon: ")
    date = datetime.strptime(input("Entrez la date du jalon (AAAA-MM-JJ): "), '%Y-%m-%d')
    return Jalon(nom, date)
