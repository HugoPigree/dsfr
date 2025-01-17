from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import BaseUserManager
import hashlib
import os

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    class Meta:
        db_table = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom


class Projets(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priorite = models.CharField(max_length=50, blank=True, null=True)
    date_debut = models.DateField(blank=True, null=True)
    date_fin_souhaitee = models.DateField(blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='projets')
    lien = models.URLField(max_length=500, blank=True, null=True)
    video = models.FileField(upload_to='uploads/videos/', blank=True, null=True)

    class Meta:
        db_table = 'projets'

    def __str__(self):
        return self.titre


class Organisation(models.Model):
    projet = models.ForeignKey(Projets, on_delete=models.CASCADE)
    sd = models.TextField(blank=True, null=True)
    moa = models.TextField(blank=True, null=True)
    moe = models.TextField(blank=True, null=True)
    prestataire = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'organisation'


class PlanningPrevisionnel(models.Model):
    projet = models.ForeignKey(Projets, on_delete=models.CASCADE)
    duree_prevue = models.TextField(blank=True, null=True)
    nombre_etp_estime = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'planning_previsionnel'


class MaturiteProjet(models.Model):
    projet = models.ForeignKey(Projets, on_delete=models.CASCADE)

    plan_de_charge = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    plan_de_charge_commentaire = models.TextField(blank=True, null=True)

    feb = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    feb_commentaire = models.TextField(blank=True, null=True)

    note_de_cadrage = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    note_de_cadrage_commentaire = models.TextField(blank=True, null=True)

    cahier_des_charges = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    cahier_des_charges_commentaire = models.TextField(blank=True, null=True)

    fonctionne = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    fonctionne_commentaire = models.TextField(blank=True, null=True)

    dat = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    dat_commentaire = models.TextField(blank=True, null=True)

    documentation_utilisateurs = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    documentation_utilisateurs_commentaire = models.TextField(blank=True, null=True)

    demande_sso = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    demande_sso_commentaire = models.TextField(blank=True, null=True)

    demande_hebergement = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    demande_hebergement_commentaire = models.TextField(blank=True, null=True)

    fiche_registre = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    fiche_registre_commentaire = models.TextField(blank=True, null=True)

    note_orientation_ssi = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    note_orientation_ssi_commentaire = models.TextField(blank=True, null=True)

    analyse_de_risque = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    analyse_de_risque_commentaire = models.TextField(blank=True, null=True)

    homologation = models.FileField(upload_to='uploads/maturite/', blank=True, null=True)
    homologation_commentaire = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'maturite_projet'



class CaracteristiquesTechniques(models.Model):
    projet = models.ForeignKey(Projets, on_delete=models.CASCADE)
    os_serveur = models.TextField(blank=True, null=True)
    type_hebergement = models.TextField(blank=True, null=True)
    techno_utilisees = models.TextField(blank=True, null=True)
    authentification = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'caracteristiques_techniques'


class Budget(models.Model):
    projet = models.ForeignKey(Projets, on_delete=models.CASCADE)
    hebergement = models.FileField(upload_to='uploads/budget/', blank=True, null=True)
    hebergement_commentaire = models.TextField(blank=True, null=True)

    homologation = models.FileField(upload_to='uploads/budget/', blank=True, null=True)
    homologation_budget_commentaire = models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'budget'



class AvancementProjet(models.Model):
    CHOIX_AVANCEMENT = [
        ("Demande", "Demande"),
        ("Cadrage", "Cadrage"),
        ("Étude de faisabilité", "Étude de faisabilité"),
        ("Conception", "Conception"),
        ("Réalisation", "Réalisation"),
        ("Déploiement", "Déploiement"),
        ("Exploitation", "Exploitation"),
    ]
    projet = models.ForeignKey(Projets, on_delete=models.CASCADE)
    choix = models.CharField(max_length=100, choices=CHOIX_AVANCEMENT)

    class Meta:
        db_table = "avancement_projet"
        verbose_name = "Avancement Projet"
        verbose_name_plural = "Avancements Projets"

    def __str__(self):
        return f"{self.projet.titre} - {self.choix}"


class Users(models.Model):
    matricule = models.CharField(max_length=7, unique=True)
    password = models.CharField(max_length=200, null=False, blank=False)  # Mot de passe en texte clair
    email = models.EmailField(unique=True, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)# Date de création de l'utilisateur

    REQUIRED_FIELDS = ["password", "email"]
    USERNAME_FIELD = "matricule"

    class Meta:
        db_table = "users_table"
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.matricule


class UserSessions(models.Model):
    user = models.ForeignKey("Users", on_delete=models.CASCADE, related_name="sessions")
    session_key = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Date de début de session
    expired_at = models.DateTimeField(blank=True, null=True)  # Date d'expiration de la session

    class Meta:
        db_table = "user_sessions"
        verbose_name = "Session utilisateur"
        verbose_name_plural = "Sessions utilisateurs"

    def __str__(self):
        return f"Session de {self.user.matricule} - {self.session_key}"
