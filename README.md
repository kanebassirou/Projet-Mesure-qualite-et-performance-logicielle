# Projet Mesure Qualité et Performance Logicielle

Ce projet vise à évaluer et améliorer la qualité et la performance du code logiciel en utilisant divers outils d'analyse statique et de tests unitaires.

## Table des Matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Tests](#tests)
- [Contributions](#contributions)
- [Licence](#licence)
- [Contact](#contact)

## Installation

Pour installer les dépendances nécessaires pour ce projet, utilisez les commandes suivantes :

```bash
# Cloner le dépôt
git clone https://github.com/votre-utilisateur/projet-mesure-qualite.git

# Naviguer dans le répertoire du projet
cd projet-mesure-qualite

# Installer les dépendances pour la mesure et qualite 
pip install flake8 
pip install pylint
pip install mypy
pip install coverage
pip install  Black
pip install pyflakes

 Utilisation
Pour analyser le code et exécuter les tests, suivez ces instructions :

1. **Analyse de code avec flake8 :**
    ```bash
    flake8 .
    ```
2. **Analyse de code avec pylint :**
    ```bash
    pylint nom_du_module/
    ```
3. **Vérification du typage statique avec mypy :**
    ```bash
    mypy nom_du_module/
    ```
4. **Exécution des tests unitaires avec couverture :**
    ```bash
    coverage run -m unittest discover
    coverage report
    ```
5. **Analyse des variables inutilisées avec vulture :**
    ```bash
    vulture nom_du_module/
    ```
6. **Reformatage du code avec Black :**
    ```bash
    black .
    ```
7. **Évaluation de la complexité cyclomatique avec radon :**
    ```bash
    radon cc nom_du_module/
    ```
8. **Vérification des erreurs de syntaxe avec pyflakes :**
    ```bash
    pyflakes nom_du_module/
    ```

## Tests
Les tests unitaires sont implémentés pour vérifier le bon fonctionnement des différentes méthodes du projet. Pour exécuter les tests, utilisez la commande suivante :
```bash
python -m unittest discover
