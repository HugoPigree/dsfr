from django.shortcuts import render
from .forms import ProjetForm
from django.shortcuts import render, redirect
from django.utils.text import slugify
# Dictionnaire des catégories et leurs projets
categories = {
    "medical": {
        "titre": "Secteur Médical",
        "description": "Liste des projets du secteur médical",
        "projets": [
            {
                "slug": "delta_medical",
                "titre": "Delta Médical",
                "description": "Modernisation des soins",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-01-01",
                    "date_fin_souhaitee": "2024-12-31",
                    "organisation": "Organisation X",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": False,
                            "fiche_registre": True,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Linux",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["Django", "React"],
                        "bdd": "PostgreSQL",
                        "authentification": "OAuth2",
                    },
                    "budget": "100,000 €",
                    "avancement_projet": "Cadrage",
                    "avancement_homologation": "Note d'orientation SSI",
                },
            },
            {
                "slug": "psycho_trauma",
                "titre": "Psycho-Trauma",
                "description": "Gestion des troubles post-traumatiques",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-02-01",
                    "date_fin_souhaitee": "2025-02-28",
                    "organisation": "Ministère de la Santé",
                    "planning_previsionnel": "14 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": True,
                            "cahier_des_charges": False,
                            "dat": True,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": True,
                            "fiche_registre": True,
                            "note_orientation_ssi": False,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Ubuntu",
                        "type_hebergement": "On-premise",
                        "techno_utilisees": ["Python", "Flask"],
                        "bdd": "MySQL",
                        "authentification": "JWT",
                    },
                    "budget": "200,000 €",
                    "avancement_projet": "Étude de faisabilité",
                    "avancement_homologation": "Analyse de risque",
                },
            },
            {
                "slug": "handicap",
                "titre": "Handicap",
                "description": "Inclusion des personnes en situation de handicap",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-06-01",
                    "date_fin_souhaitee": "2025-06-30",
                    "organisation": "Organisation Y",
                    "planning_previsionnel": "24 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": False,
                            "feb": False,
                            "note_de_cadrage": True,
                            "cahier_des_charges": False,
                            "dat": False,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": True,
                            "fiche_registre": False,
                            "note_orientation_ssi": False,
                            "analyse_de_risque": True,
                            "homologation": True,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Windows",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["PHP", "Laravel"],
                        "bdd": "PostgreSQL",
                        "authentification": "LDAP",
                    },
                    "budget": "150,000 €",
                    "avancement_projet": "Réalisation",
                    "avancement_homologation": "Socle de sécurité",
                },
            },
            {
                "slug": "pol2as",
                "titre": "POL2AS",
                "description": "Absences administratives médicales",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-03-01",
                    "date_fin_souhaitee": "2024-08-31",
                    "organisation": "Ministère de la Santé",
                    "planning_previsionnel": "6 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": False,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": True,
                            "fiche_registre": True,
                            "note_orientation_ssi": False,
                            "analyse_de_risque": False,
                            "homologation": True,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Ubuntu",
                        "type_hebergement": "Private Cloud",
                        "techno_utilisees": ["Node.js", "MongoDB"],
                        "bdd": "MongoDB",
                        "authentification": "OAuth2",
                    },
                    "budget": "50,000 €",
                    "avancement_projet": "Étude de faisabilité",
                    "avancement_homologation": "Audit",
                },
            },
            {
                "slug": "gapv",
                "titre": "GAPV",
                "description": "Gestion des alertes et prévention des vulnérabilités",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-06-01",
                    "date_fin_souhaitee": "2025-01-31",
                    "organisation": "Organisation Z",
                    "planning_previsionnel": "8 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": True,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": False,
                            "fiche_registre": False,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "CentOS",
                        "type_hebergement": "On-premise",
                        "techno_utilisees": ["Java", "Spring Boot"],
                        "bdd": "MySQL",
                        "authentification": "JWT",
                    },
                    "budget": "80,000 €",
                    "avancement_projet": "Cadrage",
                    "avancement_homologation": "Analyse de risque",
                },
            },
            {
                "slug": "sisspo",
                "titre": "Sisspo",
                "description": "Systèmes d’information et support opérationnel",
                "details": {
                    "priorite": "Basse",
                    "date_debut": "2024-09-01",
                    "date_fin_souhaitee": "2025-03-31",
                    "organisation": "Organisation A",
                    "planning_previsionnel": "7 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": True,
                            "cahier_des_charges": True,
                            "dat": True,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": False,
                            "fiche_registre": True,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Debian",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["Angular", "Node.js"],
                        "bdd": "PostgreSQL",
                        "authentification": "OAuth2",
                    },
                    "budget": "120,000 €",
                    "avancement_projet": "Déploiement",
                    "avancement_homologation": "Socle de sécurité",
                },
            },
        ],
    },
    "rh": {
        "titre": "Ressources Humaines",
        "description": "Liste des projets du secteur RH",
        "projets": [
            {
                "slug": "asa",
                "titre": "ASA",
                "description": "Gestion des absences spécifiques",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-03-01",
                    "date_fin_souhaitee": "2024-09-30",
                    "organisation": "Ministère des Ressources Humaines",
                    "planning_previsionnel": "6 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": False,
                            "note_de_cadrage": True,
                            "cahier_des_charges": False,
                            "dat": True,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": False,
                            "fiche_registre": True,
                            "note_orientation_ssi": False,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Ubuntu",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["Django", "React"],
                        "bdd": "PostgreSQL",
                        "authentification": "OAuth2",
                    },
                    "budget": "100,000 €",
                    "avancement_projet": "Cadrage",
                    "avancement_homologation": "Analyse de risque",
                },
            },
            {
                "slug": "nomenclature",
                "titre": "Nomenclature",
                "description": "Budgets opérationnels de programme",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-04-01",
                    "date_fin_souhaitee": "2025-04-30",
                    "organisation": "Ministère des Finances",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": True,
                            "fiche_registre": True,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "CentOS",
                        "type_hebergement": "On-premise",
                        "techno_utilisees": ["Node.js", "Angular"],
                        "bdd": "MySQL",
                        "authentification": "JWT",
                    },
                    "budget": "200,000 €",
                    "avancement_projet": "Étude de faisabilité",
                    "avancement_homologation": "Audit",
                },
            },
            {
                "slug": "mobipol2",
                "titre": "MOBIPOL2",
                "description": "Mobilité et gestion des postes",
                "details": {
                    "priorite": "Basse",
                    "date_debut": "2024-06-01",
                    "date_fin_souhaitee": "2025-06-30",
                    "organisation": "Ministère de la Défense",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": False,
                            "feb": True,
                            "note_de_cadrage": True,
                            "cahier_des_charges": False,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": True,
                            "fiche_registre": False,
                            "note_orientation_ssi": False,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Windows Server",
                        "type_hebergement": "Private Cloud",
                        "techno_utilisees": ["PHP", "Laravel"],
                        "bdd": "PostgreSQL",
                        "authentification": "LDAP",
                    },
                    "budget": "150,000 €",
                    "avancement_projet": "Conception",
                    "avancement_homologation": "Analyse de risque",
                },
            },
            {
                "slug": "bad",
                "titre": "BAD",
                "description": "Bases administratives de données",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-02-01",
                    "date_fin_souhaitee": "2024-07-31",
                    "organisation": "Ministère des Affaires Sociales",
                    "planning_previsionnel": "5 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": True,
                            "fiche_registre": True,
                            "note_orientation_ssi": False,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Ubuntu",
                        "type_hebergement": "On-premise",
                        "techno_utilisees": ["Java", "Spring Boot"],
                        "bdd": "MongoDB",
                        "authentification": "OAuth2",
                    },
                    "budget": "50,000 €",
                    "avancement_projet": "Réalisation",
                    "avancement_homologation": "Socle de sécurité",
                },
            },
            {
                "slug": "retraite",
                "titre": "Retraite",
                "description": "Budgets pour les retraites",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-05-01",
                    "date_fin_souhaitee": "2025-05-31",
                    "organisation": "Ministère de la Sécurité Sociale",
                    "planning_previsionnel": "13 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": False,
                            "feb": True,
                            "note_de_cadrage": True,
                            "cahier_des_charges": False,
                            "dat": True,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": True,
                            "fiche_registre": False,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": False,
                            "homologation": True,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Linux",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["Python", "Flask"],
                        "bdd": "MySQL",
                        "authentification": "LDAP",
                    },
                    "budget": "300,000 €",
                    "avancement_projet": "Conception",
                    "avancement_homologation": "Audit",
                },
            },
            {
                "slug": "pep",
                "titre": "PEP",
                "description": "Parcours des personnels",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-03-01",
                    "date_fin_souhaitee": "2024-08-31",
                    "organisation": "Ministère des Finances",
                    "planning_previsionnel": "7 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": True,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": True,
                            "fiche_registre": True,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "CentOS",
                        "type_hebergement": "On-premise",
                        "techno_utilisees": ["Java", "Spring Boot"],
                        "bdd": "PostgreSQL",
                        "authentification": "LDAP",
                    },
                    "budget": "250,000 €",
                    "avancement_projet": "Étude de faisabilité",
                    "avancement_homologation": "Note d'orientation SSI",
                },
            },
            {
                "slug": "suivi_contractuel",
                "titre": "Suivi Contractuel",
                "description": "Gestion des contrats",
                "details": {
                    "priorite": "Basse",
                    "date_debut": "2024-07-01",
                    "date_fin_souhaitee": "2025-07-31",
                    "organisation": "Ministère de l'Intérieur",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": False,
                            "feb": False,
                            "note_de_cadrage": True,
                            "cahier_des_charges": False,
                            "dat": False,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": True,
                            "fiche_registre": False,
                            "note_orientation_ssi": False,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Windows Server",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["PHP", "Laravel"],
                        "bdd": "MongoDB",
                        "authentification": "OAuth2",
                    },
                    "budget": "200,000 €",
                    "avancement_projet": "Réalisation",
                    "avancement_homologation": "Audit",
                },
            },
            {
                "slug": "avancement",
                "titre": "Avancement",
                "description": "Gestion des mutations et avancements",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-04-01",
                    "date_fin_souhaitee": "2025-04-30",
                    "organisation": "Ministère des Ressources Humaines",
                    "planning_previsionnel": "13 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": False,
                            "fiche_registre": True,
                            "note_orientation_ssi": False,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Ubuntu",
                        "type_hebergement": "Private Cloud",
                        "techno_utilisees": ["Node.js", "React"],
                        "bdd": "MySQL",
                        "authentification": "JWT",
                    },
                    "budget": "350,000 €",
                    "avancement_projet": "Conception",
                    "avancement_homologation": "Socle de sécurité",
                },
            },
            {
                "slug": "choix_poste",
                "titre": "Choix Poste Officier",
                "description": "Choix des postes pour les officiers",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-02-01",
                    "date_fin_souhaitee": "2024-08-31",
                    "organisation": "Ministère de la Défense",
                    "planning_previsionnel": "7 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": True,
                            "fiche_registre": False,
                            "note_orientation_ssi": False,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "CentOS",
                        "type_hebergement": "On-premise",
                        "techno_utilisees": ["Java", "Spring Boot"],
                        "bdd": "PostgreSQL",
                        "authentification": "LDAP",
                    },
                    "budget": "450,000 €",
                    "avancement_projet": "Réalisation",
                    "avancement_homologation": "Socle de sécurité",
                },
            },
        ],
    },
    "autres": {
        "titre": "Secteur Divers",
        "description": "Liste des projets du secteur divers",
        "projets": [
            {
                "slug": "tigre",
                "titre": "TIGRE",
                "description": "Projet d'amélioration",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-05-01",
                    "date_fin_souhaitee": "2025-05-31",
                    "organisation": "Ministère de l'Environnement",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": False,
                            "note_de_cadrage": True,
                            "cahier_des_charges": False,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": True,
                            "fiche_registre": False,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Linux",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["Python", "Flask"],
                        "bdd": "MongoDB",
                        "authentification": "OAuth2",
                    },
                    "budget": "80,000 €",
                    "avancement_projet": "Conception",
                    "avancement_homologation": "Analyse de risque",
                },
            },
            {
                "slug": "cartographie",
                "titre": "Cartographie",
                "description": "Projet de cartographie",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-06-01",
                    "date_fin_souhaitee": "2025-06-30",
                    "organisation": "Ministère des Transports",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": True,
                            "fiche_registre": True,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Windows Server",
                        "type_hebergement": "Private Cloud",
                        "techno_utilisees": ["Java", "Spring Boot"],
                        "bdd": "PostgreSQL",
                        "authentification": "LDAP",
                    },
                    "budget": "120,000 €",
                    "avancement_projet": "Étude de faisabilité",
                    "avancement_homologation": "Audit",
                },
            },
            {
                "slug": "ecologie",
                "titre": "Écologie",
                "description": "Projet écologique",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-07-01",
                    "date_fin_souhaitee": "2025-07-31",
                    "organisation": "Ministère de l'Écologie",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": True,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": False,
                            "fiche_registre": True,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Ubuntu",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["Django", "React"],
                        "bdd": "MongoDB",
                        "authentification": "OAuth2",
                    },
                    "budget": "150,000 €",
                    "avancement_projet": "Cadrage",
                    "avancement_homologation": "Socle de sécurité",
                },
            },
        ],
    },
    "drhfs": {
        "titre": "Secteur DRHFS",
        "description": "Liste des projets du secteur DRHFS",
        "projets": [
            {
                "slug": "gedem_2",
                "titre": "GEDEM 2",
                "description": "Projet GEDEM 2",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-02-01",
                    "date_fin_souhaitee": "2025-01-31",
                    "organisation": "Ministère des Ressources Humaines",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": True,
                            "cahier_des_charges": False,
                            "dat": True,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": True,
                            "fiche_registre": True,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Linux",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["Django", "React"],
                        "bdd": "PostgreSQL",
                        "authentification": "OAuth2",
                    },
                    "budget": "150,000 €",
                    "avancement_projet": "Conception",
                    "avancement_homologation": "Analyse de risque",
                },
            },
            {
                "slug": "oeb",
                "titre": "OEB",
                "description": "Projet OEB",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-03-01",
                    "date_fin_souhaitee": "2024-12-31",
                    "organisation": "Ministère de l'Éducation Nationale",
                    "planning_previsionnel": "10 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": False,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": True,
                            "fiche_registre": False,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Windows Server",
                        "type_hebergement": "On-premise",
                        "techno_utilisees": ["PHP", "Laravel"],
                        "bdd": "MySQL",
                        "authentification": "LDAP",
                    },
                    "budget": "200,000 €",
                    "avancement_projet": "Étude de faisabilité",
                    "avancement_homologation": "Audit",
                },
            },
            {
                "slug": "co_working",
                "titre": "Co-Working",
                "description": "Projet Co-Working",
                "details": {
                    "priorite": "Basse",
                    "date_debut": "2024-05-01",
                    "date_fin_souhaitee": "2025-04-30",
                    "organisation": "Ministère des Affaires Sociales",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": True,
                            "cahier_des_charges": False,
                            "dat": False,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": False,
                            "fiche_registre": True,
                            "note_orientation_ssi": False,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Ubuntu",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["Java", "Spring Boot"],
                        "bdd": "PostgreSQL",
                        "authentification": "OAuth2",
                    },
                    "budget": "100,000 €",
                    "avancement_projet": "Déploiement",
                    "avancement_homologation": "Socle de sécurité",
                },
            },
        ],
    },
    "utilisateurs": {
        "titre": "Secteur Utilisateurs",
        "description": "Liste des projets du secteur utilisateurs",
        "projets": [
            {
                "slug": "ares",
                "titre": "ARES",
                "description": "Projet ARES",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-09-01",
                    "date_fin_souhaitee": "2025-09-30",
                    "organisation": "Ministère de la Défense",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": True,
                            "fiche_registre": False,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Linux",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["Java", "Spring Boot"],
                        "bdd": "MySQL",
                        "authentification": "OAuth2",
                    },
                    "budget": "100,000 €",
                    "avancement_projet": "Conception",
                    "avancement_homologation": "Analyse de risque",
                },
            },
            {
                "slug": "osadis",
                "titre": "OSADIS",
                "description": "Projet OSADIS",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-08-01",
                    "date_fin_souhaitee": "2025-08-31",
                    "organisation": "Ministère de l'Intérieur",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": False,
                            "note_de_cadrage": True,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": True,
                            "fiche_registre": True,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Windows Server",
                        "type_hebergement": "On-Premise",
                        "techno_utilisees": ["Python", "Flask"],
                        "bdd": "PostgreSQL",
                        "authentification": "LDAP",
                    },
                    "budget": "120,000 €",
                    "avancement_projet": "Étude de faisabilité",
                    "avancement_homologation": "Audit",
                },
            },
            {
                "slug": "thesaurus",
                "titre": "THESAURUS",
                "description": "Projet Thesaurus",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-07-01",
                    "date_fin_souhaitee": "2025-07-31",
                    "organisation": "Ministère de la Culture",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": True,
                            "cahier_des_charges": True,
                            "dat": True,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": False,
                            "fiche_registre": True,
                            "note_orientation_ssi": False,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Ubuntu",
                        "type_hebergement": "Private Cloud",
                        "techno_utilisees": ["Django", "React"],
                        "bdd": "MongoDB",
                        "authentification": "OAuth2",
                    },
                    "budget": "150,000 €",
                    "avancement_projet": "Cadrage",
                    "avancement_homologation": "Socle de sécurité",
                },
            },
            {
                "slug": "siag_ng",
                "titre": "SIAG-NG",
                "description": "Projet SIAG-NG",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-09-01",
                    "date_fin_souhaitee": "2025-09-30",
                    "organisation": "Ministère des Finances",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": False,
                            "note_de_cadrage": True,
                            "cahier_des_charges": False,
                            "dat": False,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": False,
                            "fiche_registre": True,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Linux",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["Django", "Vue.js"],
                        "bdd": "MySQL",
                        "authentification": "OAuth2",
                    },
                    "budget": "200,000 €",
                    "avancement_projet": "Réalisation",
                    "avancement_homologation": "Dossier d'architecture",
                },
            },
            {
                "slug": "maarch",
                "titre": "MAARCH",
                "description": "Projet Maarch",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-06-01",
                    "date_fin_souhaitee": "2025-06-30",
                    "organisation": "Ministère de l'Éducation Nationale",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": True,
                            "fiche_registre": True,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Windows Server",
                        "type_hebergement": "On-Premise",
                        "techno_utilisees": ["PHP", "Laravel"],
                        "bdd": "Oracle",
                        "authentification": "LDAP",
                    },
                    "budget": "90,000 €",
                    "avancement_projet": "Conception",
                    "avancement_homologation": "Avis de décision d'homologation",
                },
            },
            {
                "slug": "geopol",
                "titre": "GEOPOL",
                "description": "Projet Geopol",
                "details": {
                    "priorite": "Haute",
                    "date_debut": "2024-07-01",
                    "date_fin_souhaitee": "2025-07-31",
                    "organisation": "Ministère des Affaires Étrangères",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": True,
                            "cahier_des_charges": True,
                            "dat": True,
                            "documentation_utilisateurs": False,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": False,
                            "demande_hebergement": True,
                            "fiche_registre": False,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": True,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Ubuntu",
                        "type_hebergement": "Private Cloud",
                        "techno_utilisees": ["Node.js", "Vue.js"],
                        "bdd": "PostgreSQL",
                        "authentification": "OAuth2",
                    },
                    "budget": "110,000 €",
                    "avancement_projet": "Réalisation",
                    "avancement_homologation": "Audit",
                },
            },
            {
                "slug": "gestt",
                "titre": "GestTT",
                "description": "Projet GestTT",
                "details": {
                    "priorite": "Moyenne",
                    "date_debut": "2024-05-01",
                    "date_fin_souhaitee": "2025-05-31",
                    "organisation": "Ministère de la Recherche",
                    "planning_previsionnel": "12 mois",
                    "maturite": {
                        "dossier_fonctionnel": {
                            "plan_de_charge": True,
                            "feb": True,
                            "note_de_cadrage": False,
                            "cahier_des_charges": True,
                            "dat": False,
                            "documentation_utilisateurs": True,
                        },
                        "dossier_si_et_ssi": {
                            "demande_sso": True,
                            "demande_hebergement": False,
                            "fiche_registre": True,
                            "note_orientation_ssi": True,
                            "analyse_de_risque": False,
                            "homologation": False,
                        },
                    },
                    "caracteristiques_techniques": {
                        "os_serveur": "Windows Server",
                        "type_hebergement": "Cloud",
                        "techno_utilisees": ["Python", "Django"],
                        "bdd": "SQLite",
                        "authentification": "LDAP",
                    },
                    "budget": "95,000 €",
                    "avancement_projet": "Cadrage",
                    "avancement_homologation": "Note d'orientation SSI",
                },
            },
        ],
    },
}


# Vue pour la page d'accueil
def index(request):
    return render(request, "projet_centrale_app/index.html")


# Vue pour les catégories dynamiques
def categorie_detail(request, categorie_slug):
    categorie = categories.get(categorie_slug)
    print(f"Slug transmis : {categorie_slug}")
    categorie = categories.get(categorie_slug)
    print(f"Catégorie récupérée : {categorie}")
    if not categorie:
        return render(request, "404.html", status=404)
    return render(
        request,
        "projet_centrale_app/categories_projets.html",
        {
            "categorie": categorie,
            "categorie_slug": categorie_slug,  # Ajout de categorie_slug
        },
    )


# Vue pour les détails des projets
def projet_detail(request, categorie_slug, projet_slug):
    projet = None
    # Rechercher le projet correspondant dans la bonne catégorie
    for categorie_key, categorie in categories.items():
        if categorie_key == categorie_slug:
            projet = next(
                (p for p in categorie["projets"] if p["slug"] == projet_slug), None
            )
            break

    if not projet:
        return render(request, "404.html", status=404)

    # Passer le projet et la catégorie au template
    return render(
        request,
        "projet_centrale_app/projet_detail.html",
        {"projet": projet, "categorie_slug": categorie_slug},
    )


# Vue pour la page info_projet
def info_projet(request, categorie_slug, projet_slug):
    projet = None
    for key, categorie in categories.items():
        if key == categorie_slug:
            projet = next(
                (p for p in categorie["projets"] if p["slug"] == projet_slug), None
            )
            break

    if not projet:
        return render(request, "404.html", status=404)

    # Récupérer les détails spécifiques au projet
    details_projet = projet.get("details", {})

    return render(
        request,
        "projet_centrale_app/info_projet.html",
        {
            "projet": projet,
            "details_projet": details_projet,
        },
    )

def ajouter_projet(request):
    if request.method == "POST":
        form = ProjetForm(request.POST)
        if form.is_valid():
            projet_data = form.cleaned_data
            titre = projet_data["titre"]

            # Génération automatique du slug (titre adapter pour l'ordi)
            slug = slugify(titre)

            # Ajouter le projet au dictionnaire existant
            categorie_slug = projet_data["categorie_slug"]
            if categorie_slug in categories:
                categories[categorie_slug]["projets"].append({
                    "slug": slug,
                    "titre": titre,
                    "description": projet_data["description"],
                    "details": {
                        "priorite": projet_data["priorite"],
                        "date_debut": projet_data["date_debut"],
                        "date_fin_souhaitee": projet_data["date_fin_souhaitee"],
                        "organisation": projet_data["organisation"],
                        "planning_previsionnel": projet_data["planning_previsionnel"],
                        "maturite": {
                            "dossier_fonctionnel": {
                                "plan_de_charge": projet_data["plan_de_charge"],
                                "feb": projet_data["feb"],
                                "note_de_cadrage": projet_data["note_de_cadrage"],
                                "cahier_des_charges": projet_data["cahier_des_charges"],
                                "dat": projet_data["dat"],
                                "documentation_utilisateurs": projet_data["documentation_utilisateurs"],
                            },
                            "dossier_si_et_ssi": {
                                "demande_sso": projet_data["demande_sso"],
                                "demande_hebergement": projet_data["demande_hebergement"],
                                "fiche_registre": projet_data["fiche_registre"],
                                "note_orientation_ssi": projet_data["note_orientation_ssi"],
                                "analyse_de_risque": projet_data["analyse_de_risque"],
                                "homologation": projet_data["homologation"],
                            },
                        },
                        "caracteristiques_techniques": {
                            "os_serveur": projet_data["os_serveur"],
                            "type_hebergement": projet_data["type_hebergement"],
                            "techno_utilisees": projet_data["techno_utilisees"],
                            "bdd": projet_data["bdd"],
                            "authentification": projet_data["authentification"],
                        },
                        "budget": projet_data["budget"],
                        "avancement_projet": projet_data["avancement_projet"],
                        "avancement_homologation": projet_data["avancement_homologation"],
                    },
                })
                return redirect('index')  # Retourner à la page d'accueil
            else:
                return render(request, "404.html", status=404)
    else:
        form = ProjetForm()
    return render(request, "projet_centrale_app/ajouter_projet.html", {"form": form})