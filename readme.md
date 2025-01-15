# DSFR Project

Ce projet est basé sur Django et utilise DSFR pour le design. Il permet la gestion des projets dans un environnement professionnel.

## Fonctionnalités

- Gestion des projets (ajout, modification, suppression).
- Authentification avec rôles (admin/utilisateur).
- Téléchargement de vidéos et pièces jointes.

## Prérequis

- Python 3.x
- Django 4.x
- Node.js (pour Tailwind CSS)
- Un environnement virtuel (recommandé)

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/HugoPigree/dsfr.git
   cd dsfr

   pip install -r requirements.txt

2. Initialiser la BDD :
   ```bash
   python manage.py migrate
   
3. Lancez le serveur :
   ```bash
   python manage.py runserver

