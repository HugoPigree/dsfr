from django import forms

class ProjetForm(forms.Form):
    # Champs principaux
    titre = forms.CharField(label="Titre", max_length=255)

    description = forms.CharField(widget=forms.Textarea, label="Description")

    # Catégorie
    categorie_slug = forms.ChoiceField(
        choices=[
            ('medical', 'Médical'),
            ('rh', 'RH'),
            ('autres', 'Autres'),
            ('drhfs', 'DRHFS'),
            ('utilisateurs', 'Utilisateurs'),
        ],
        label="Catégorie"
    )

    # Détails du projet
    priorite = forms.ChoiceField(choices=[('Haute', 'Haute'), ('Moyenne', 'Moyenne'), ('Basse', 'Basse')])
    date_debut = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date de début")
    date_fin_souhaitee = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date de fin souhaitée")
    organisation = forms.CharField(label="Organisation", max_length=255)
    planning_previsionnel = forms.CharField(label="Planning prévisionnel", max_length=255)
    budget = forms.CharField(label="Budget", max_length=50)

    # Maturité - Dossier fonctionnel
    plan_de_charge = forms.BooleanField(label="Plan de charge", required=False)
    feb = forms.BooleanField(label="FEB", required=False)
    note_de_cadrage = forms.BooleanField(label="Note de cadrage", required=False)
    cahier_des_charges = forms.BooleanField(label="Cahier des charges", required=False)
    dat = forms.BooleanField(label="DAT", required=False)
    documentation_utilisateurs = forms.BooleanField(label="Documentation utilisateurs", required=False)

    # Maturité - Dossier SI et SSI
    demande_sso = forms.BooleanField(label="Demande SSO", required=False)
    demande_hebergement = forms.BooleanField(label="Demande d'hébergement", required=False)
    fiche_registre = forms.BooleanField(label="Fiche registre", required=False)
    note_orientation_ssi = forms.BooleanField(label="Note d'orientation SSI", required=False)
    analyse_de_risque = forms.BooleanField(label="Analyse de risque", required=False)
    homologation = forms.BooleanField(label="Homologation", required=False)

    # Caractéristiques techniques
    os_serveur = forms.CharField(label="OS Serveur", max_length=50)
    type_hebergement = forms.CharField(label="Type d'hébergement", max_length=50)
    techno_utilisees = forms.CharField(widget=forms.Textarea, label="Technologies utilisées")
    bdd = forms.CharField(label="Base de données", max_length=50)
    authentification = forms.CharField(label="Authentification", max_length=50)

    # Avancements
    avancement_projet = forms.ChoiceField(
        choices=[
            ('Demande', 'Demande'),
            ('Cadrage', 'Cadrage'),
            ('Étude de faisabilité', 'Étude de faisabilité'),
            ('Déploiement', 'Déploiement'),
            ('Conception', 'Conception'),
            ('Réalisation', 'Réalisation'),
            ('Exploitation', 'Exploitation'),
        ],
        label="Avancement du projet"
    )
    avancement_homologation = forms.ChoiceField(
        choices=[
            ('Note d\'orientation SSI', 'Note d\'orientation SSI'),
            ('Analyse de risque', 'Analyse de risque'),
            ('Socle de sécurité', 'Socle de sécurité'),
            ('Dossier d\'architecture', 'Dossier d\'architecture'),
            ('Audit', 'Audit'),
            ('Avis de décision d\'homologation', 'Avis de décision d\'homologation'),
        ],
        label="Avancement de l'homologation"
    )
