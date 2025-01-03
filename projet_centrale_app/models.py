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
    plan_de_charge = models.TextField(blank=True, null=True)
    feb = models.TextField(blank=True, null=True)
    note_de_cadrage = models.TextField(blank=True, null=True)
    cahier_des_charges = models.TextField(blank=True, null=True)
    fonctionne = models.TextField(blank=True, null=True)
    dat = models.TextField(blank=True, null=True)
    documentation_utilisateurs = models.TextField(blank=True, null=True)
    demande_sso = models.TextField(blank=True, null=True)
    demande_hebergement = models.TextField(blank=True, null=True)
    fiche_registre = models.TextField(blank=True, null=True)
    note_orientation_ssi = models.TextField(blank=True, null=True)
    analyse_de_risque = models.TextField(blank=True, null=True)
    homologation = models.TextField(blank=True, null=True)

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
    hebergement = models.TextField(blank=True, null=True)
    homologation = models.TextField(blank=True, null=True)

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





class UsersManagers(BaseUserManager):
    def get_by_natural_key(self, matricule):
        return self.get(matricule=matricule)

    def create_user(self, matricule, password=None):
        if not matricule:
            return {"error": "matricule est requis"}

        if self.model.objects.filter(matricule=matricule).exists():
            return {"error": "matricule existe déjà"}

        user = self.model(matricule=matricule)
        user.set_password(password)
        user.save(using=self._db)
        success = " créé avec succès"
        return {"user": user, "success": success}

class Users(models.Model):
    matricule = models.CharField(max_length=7, unique=True)
    password = models.CharField(max_length=250, null=False, blank=False)
    REQUIRED_FIELDS = ["password"]
    USERNAME_FIELD = "matricule"

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def set_password(self, raw_password):
        self.password = hashlib.sha256(
            raw_password.join(self.matricule).encode("utf-8")
        ).hexdigest()

    def check_password(self, raw_password):
        return (
            self.password
            == hashlib.sha256(raw_password.join(self.matricule).encode("utf-8")).hexdigest()
        )

    objects = UsersManagers()

    class Meta:
        db_table = "users_table"