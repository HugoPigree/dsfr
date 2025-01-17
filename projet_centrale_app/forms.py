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
            "lien",
            "video",
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
            "plan_de_charge_commentaire",
            "feb",
            "feb_commentaire",
            "note_de_cadrage",
            "note_de_cadrage_commentaire",
            "cahier_des_charges",
            "cahier_des_charges_commentaire",
            "fonctionne",
            "fonctionne_commentaire",
            "dat",
            "dat_commentaire",
            "documentation_utilisateurs",
            "documentation_utilisateurs_commentaire",
            "demande_sso",
            "demande_sso_commentaire",
            "demande_hebergement",
            "demande_hebergement_commentaire",
            "fiche_registre",
            "fiche_registre_commentaire",
            "note_orientation_ssi",
            "note_orientation_ssi_commentaire",
            "analyse_de_risque",
            "analyse_de_risque_commentaire",
            "homologation",
            "homologation_commentaire",
        ]
        widgets = {
            "plan_de_charge": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "feb": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "note_de_cadrage": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "cahier_des_charges": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "fonctionne": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "dat": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "documentation_utilisateurs": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "demande_sso": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "demande_hebergement": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "fiche_registre": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "note_orientation_ssi": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "analyse_de_risque": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "homologation": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "plan_de_charge_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "feb_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "note_de_cadrage_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "cahier_des_charges_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "fonctionne_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "dat_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "documentation_utilisateurs_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "demande_sso_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "demande_hebergement_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "fiche_registre_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "note_orientation_ssi_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "analyse_de_risque_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "homologation_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
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
        fields = [
            "hebergement",
            "hebergement_commentaire",
            "homologation",
            "homologation_budget_commentaire",
        ]
        widgets = {
            "hebergement": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "homologation": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "hebergement_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "homologation_budget_commentaire": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
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
        max_length=7,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Matricule"}),
        label="Matricule"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Mot de passe"}),
        label="Mot de passe"
    )