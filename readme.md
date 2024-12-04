## 🚀 Fonctionnalités principales

- **Navigation par catégories** : Accédez facilement aux projets selon leur catégorie.
- **Ajout de projets** : Ajoutez de nouveaux projets directement depuis l'interface utilisateur.
- **Informations détaillées** : Consultez les détails de chaque projet.

---

## 🛠️ Installation et configuration

Suivez ces étapes pour installer et lancer le projet sur votre machine locale.

### 1. Prérequis

Avant de commencer, assurez-vous d'avoir installé sur votre PC :

- **Python** (version 3.8 ou supérieure)


### 2. Cloner le projet

Clonez ce dépôt Git sur votre machine locale :

```bash
git clone https://github.com/HugoPigree/dsfr.git
cd projet-centrale

```



### Installez dependances : 

``pip install -r requirements.txt
``

### initialiser la bdd : 
``python manage.py makemigrations
python manage.py migrate
``
### Lancez le serveur local pour tester l'application :

``python manage.py runserver``