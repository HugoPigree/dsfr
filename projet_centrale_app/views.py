from django.shortcuts import render

# Dictionnaire des catégories et leurs projets
categories = {
    "medical": {
        "titre": "Secteur Médical",
        "description": "Liste des projets du secteur médical",
        "projets": [
            {"slug": "delta_medical", "titre": "Delta Médical", "description": "Modernisation des soins"},
            {"slug": "psycho_trauma", "titre": "Psycho-Trauma", "description": "Gestion des troubles post-traumatiques"},
            {"slug": "handicap", "titre": "Handicap", "description": "Inclusion des personnes en situation de handicap"},
            {"slug": "pol2as", "titre": "POL2AS", "description": "Absences administratives médicales"},
            {"slug": "gapv", "titre": "GAPV", "description": "Gestion des alertes et prévention des vulnérabilités"},
            {"slug": "sisspo", "titre": "Sisspo", "description": "Systèmes d’information et support opérationnel"},
        ],
    },
    "rh": {
        "titre": "Ressources Humaines",
        "description": "Liste des projets du secteur RH",
        "projets": [
            {"slug": "asa", "titre": "ASA", "description": "Gestion des absences spécifiques"},
            {"slug": "nomenclature", "titre": "Nomenclature", "description": "Budgets opérationnels de programme"},
            {"slug": "mobipol2", "titre": "MOBIPOL2", "description": "Mobilité et gestion des postes"},
            {"slug": "bad", "titre": "BAD", "description": "Bases administratives de données"},
            {"slug": "retraite", "titre": "Retraite", "description": "Budgets pour les retraites"},
            {"slug": "pep", "titre": "PEP", "description": "Parcours des personnels"},
            {"slug": "suivi_contractuel", "titre": "Suivi Contractuel", "description": "Gestion des contrats"},
            {"slug": "avancement", "titre": "Avancement", "description": "Gestion des mutations et avancements"},
            {"slug": "choix_poste", "titre": "Choix Poste Officier", "description": "Choix des postes pour les officiers"},
        ],
    },
    "autres": {
        "titre": "Secteur Divers",
        "description": "Liste des projets du secteur divers",
        "projets": [
            {"slug": "tigre", "titre": "TIGRE", "description": "Description du projet TIGRE"},
            {"slug": "cartographie", "titre": "Cartographie", "description": "Description du projet Cartographie"},
            {"slug": "ecologie", "titre": "Écologie", "description": "Description du projet Écologie"},
        ],
    },
    "utilisateurs": {
        "titre": "Secteur Utilisateurs",
        "description": "Liste des projets du secteur utilisateurs",
        "projets": [
            {"slug": "ares", "titre": "ARES", "description": "Description du projet ARES"},
            {"slug": "osadis", "titre": "OSADIS", "description": "Description du projet OSADIS"},
            {"slug": "thesaurus", "titre": "THESAURUS", "description": "Description du projet THESAURUS"},
            {"slug": "siag_ng", "titre": "SIAG-NG", "description": "Description du projet SIAG-NG"},
            {"slug": "maarch", "titre": "MAARCH", "description": "Description du projet MAARCH"},
            {"slug": "geopol", "titre": "GEOPOL", "description": "Description du projet GEOPOL"},
            {"slug": "gestt", "titre": "GestTT", "description": "Description du projet GestTT"},
        ],
    },
    "drhfs": {
        "titre": "Secteur DRHFS",
        "description": "Liste des projets du secteur DRHFS",
        "projets": [
            {"slug": "gedem2", "titre": "GEDEM 2", "description": "Description du projet GEDEM 2"},
            {"slug": "oeb", "titre": "OEB", "description": "Description du projet OEB"},
            {"slug": "co_working", "titre": "Co-Working", "description": "Description du projet Co-Working"},
        ],
    },
}

# Vue pour afficher les catégories dynamiques
def categorie_detail(request, categorie_slug):
    categorie = categories.get(categorie_slug)
    if not categorie:
        return render(request, "404.html", status=404)
    return render(request, "projet_centrale_app/categories_projets.html", {"categorie": categorie})

# Vue pour afficher les détails des projets
def projet_detail(request, projet_slug):
    # Recherche du projet dans les catégories
    projet = None
    categorie_slug = None
    for key, categorie in categories.items():
        for p in categorie["projets"]:
            if p["slug"] == projet_slug:
                projet = p
                categorie_slug = key
                break
        if projet:
            break

    if not projet or not categorie_slug:
        return render(request, "404.html", status=404)

    return render(
        request,
        "projet_centrale_app/projet_detail.html",
        {"projet": projet, "categorie_slug": categorie_slug}
    )

# Vue pour la page d'accueil
def index(request):
    return render(request, 'projet_centrale_app/index.html')

# Vue pour la page info_projet
def info_projet(request, categorie_slug, projet_slug):
    # Recherche du projet dans la catégorie donnée
    projet = None
    for key, categorie in categories.items():
        if key == categorie_slug:
            for p in categorie["projets"]:
                if p["slug"] == projet_slug:
                    projet = p
                    break

    return render(request, "projet_centrale_app/info_projet.html", {"projet": projet})
