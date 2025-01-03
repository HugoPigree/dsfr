from django import forms


from django.forms.widgets import DateInput
from django.utils.safestring import mark_safe

from .models import (
    Projets,
    Organisation,
    PlanningPrevisionnel,
    MaturiteProjet,
    CaracteristiquesTechniques,
    Budget,
    AvancementProjet,

    Categorie,
)

# Widget personnalisé pour les champs de type date
class DateInput(forms.DateInput):
    input_type = 'date'

# Formulaire pour le modèle Projets
class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projets
        fields = [
            "titre",
            "description",
            "priorite",
            "date_debut",
            "date_fin_souhaitee",
            "categorie",
        ]
        widgets = {
            "date_debut": DateInput(attrs={"class": "form-control", "placeholder": "jj/mm/aaaa"}),
            "date_fin_souhaitee": DateInput(attrs={"class": "form-control", "placeholder": "jj/mm/aaaa"}),
        }

# Formulaire pour le modèle Organisation
class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ["sd", "moa", "moe", "prestataire"]
        widgets = {
            "sd": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "moa": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "moe": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "prestataire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
        }

# Formulaire pour le modèle PlanningPrevisionnel
class PlanningForm(forms.ModelForm):
    class Meta:
        model = PlanningPrevisionnel
        fields = ["duree_prevue", "nombre_etp_estime"]
        widgets = {
            "duree_prevue": forms.Textarea(attrs={"class": "form-control", "rows": 2}),  # Zone de texte
            "nombre_etp_estime": forms.NumberInput(attrs={"class": "form-control"}),
        }

# Formulaire pour le modèle MaturiteProjet
class MaturiteForm(forms.ModelForm):
    class Meta:
        model = MaturiteProjet
        fields = [
            "plan_de_charge",
            "feb",
            "note_de_cadrage",
            "cahier_des_charges",
            "fonctionne",
            "dat",
            "documentation_utilisateurs",
            "demande_sso",
            "demande_hebergement",
            "fiche_registre",
            "note_orientation_ssi",
            "analyse_de_risque",
            "homologation",
        ]
        widgets = {
            field: forms.Textarea(attrs={"class": "form-control", "rows": 2}) for field in fields
        }

# Formulaire pour le modèle CaracteristiquesTechniques
class CaracteristiquesForm(forms.ModelForm):
    class Meta:
        model = CaracteristiquesTechniques
        fields = [
            "os_serveur",
            "type_hebergement",
            "techno_utilisees",
            "authentification",
        ]
        widgets = {
            "os_serveur": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "type_hebergement": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "techno_utilisees": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "authentification": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
        }

# Formulaire pour le modèle Budget
class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ["hebergement", "homologation"]
        widgets = {
            "hebergement": forms.Textarea(attrs={"class": "form-control", "rows": 2}),  # Zone de texte
            "homologation": forms.Textarea(attrs={"class": "form-control", "rows": 2}),  # Zone de texte
        }

# Formulaire pour le modèle AvancementProjet
class AvancementForm(forms.ModelForm):
    class Meta:
        model = AvancementProjet
        fields = ["choix"]
        widgets = {
            "choix": forms.Select(attrs={"class": "form-select"}),
        }



class LoginForm(forms.Form):
    matricule = forms.CharField(
        label="Matricule",
        max_length=7,
        widget=forms.TextInput(attrs={
            "class": "fr-input",  # Classe DSFR
            "placeholder": "Matricule",
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        max_length=100,
        widget=forms.PasswordInput(attrs={
            "class": "fr-input",  # Classe DSFR
            "placeholder": "Mot de passe",
        })
    )

class CreateUsersForm(forms.Form):
    matricule = forms.CharField(
        label="Matricule",
        max_length=7,
        widget=forms.TextInput(attrs={
            "class": "fr-input",  # Classe DSFR
            "placeholder": "Insérer matricule",
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        max_length=100,
        widget=forms.PasswordInput(attrs={
            "class": "fr-input",  # Classe DSFR
            "placeholder": "Insérer mot de passe",
        })
    )