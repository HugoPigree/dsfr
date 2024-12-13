from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
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
from .forms import (
    ProjetForm,
    OrganisationForm,
    PlanningForm,
    MaturiteForm,
    CaracteristiquesForm,
    BudgetForm,
    AvancementForm,
)
from django.urls import reverse

# Vue pour la page d'accueil
def index(request):
    categories = Categorie.objects.prefetch_related('projets').all()
    return render(request, "projet_centrale_app/index.html", {"categories": categories})

# Vue pour afficher les projets par catégorie
def categorie_detail(request, categorie_slug):
    categorie = get_object_or_404(Categorie, slug=categorie_slug)
    projets = Projets.objects.filter(categorie=categorie)
    return render(
        request,
        "projet_centrale_app/categories_projets.html",
        {"categorie": categorie, "projets": projets},
    )

# Vue pour les détails d'un projet
def projet_detail(request, projet_id):
    projet = get_object_or_404(Projets, id=projet_id)
    categorie = projet.categorie
    return render(
        request,
        "projet_centrale_app/projet_detail.html",
        {"projet": projet, "categorie": categorie},
    )

# Vue pour les informations complètes du projet
def info_projet(request, projet_id):
    projet = get_object_or_404(Projets, id=projet_id)
    organisation = Organisation.objects.filter(projet=projet).first()
    planning = PlanningPrevisionnel.objects.filter(projet=projet).first()
    maturite = MaturiteProjet.objects.filter(projet=projet).first()
    caracteristiques = CaracteristiquesTechniques.objects.filter(projet=projet).first()
    budget = Budget.objects.filter(projet=projet).first()
    avancement_projet = AvancementProjet.objects.filter(projet=projet).first()


    return render(
        request,
        "projet_centrale_app/info_projet.html",
        {
            "projet": projet,
            "organisation": organisation,
            "planning": planning,
            "maturite": maturite,
            "caracteristiques": caracteristiques,
            "budget": budget,
            "avancement_projet": avancement_projet,

        },
    )

# Vue pour ajouter un projet
def ajouter_projet(request):
    if request.method == "POST":
        projet_form = ProjetForm(request.POST)
        organisation_form = OrganisationForm(request.POST)
        planning_form = PlanningForm(request.POST)
        maturite_form = MaturiteForm(request.POST)
        caracteristiques_form = CaracteristiquesForm(request.POST)
        budget_form = BudgetForm(request.POST)
        avancement_projet_form = AvancementForm(request.POST)


        if (
            projet_form.is_valid()
            and organisation_form.is_valid()
            and planning_form.is_valid()
            and maturite_form.is_valid()
            and caracteristiques_form.is_valid()
            and budget_form.is_valid()
            and avancement_projet_form.is_valid()

        ):
            projet = projet_form.save()
            organisation = organisation_form.save(commit=False)
            organisation.projet = projet
            organisation.save()

            planning = planning_form.save(commit=False)
            planning.projet = projet
            planning.save()

            maturite = maturite_form.save(commit=False)
            maturite.projet = projet
            maturite.save()

            caracteristiques = caracteristiques_form.save(commit=False)
            caracteristiques.projet = projet
            caracteristiques.save()

            budget = budget_form.save(commit=False)
            budget.projet = projet
            budget.save()

            avancement_projet = avancement_projet_form.save(commit=False)
            avancement_projet.projet = projet
            avancement_projet.save()



            return redirect("index")
        else:
            # Log errors for debugging
            print("Projet Form Errors:", projet_form.errors)
            print("Organisation Form Errors:", organisation_form.errors)
            print("Planning Form Errors:", planning_form.errors)
            print("Maturité Form Errors:", maturite_form.errors)
            print("Caractéristiques Form Errors:", caracteristiques_form.errors)
            print("Budget Form Errors:", budget_form.errors)
            print("Avancement Projet Form Errors:", avancement_projet_form.errors)
            print("Avancement Homologation Form Errors:", avancement_homologation_form.errors)
            print("POST Data:", request.POST)
    else:
        projet_form = ProjetForm()
        organisation_form = OrganisationForm()
        planning_form = PlanningForm()
        maturite_form = MaturiteForm()
        caracteristiques_form = CaracteristiquesForm()
        budget_form = BudgetForm()
        avancement_projet_form = AvancementForm()


    return render(
        request,
        "projet_centrale_app/ajouter_projet.html",
        {
            "projet_form": projet_form,
            "organisation_form": organisation_form,
            "planning_form": planning_form,
            "maturite_form": maturite_form,
            "caracteristiques_form": caracteristiques_form,
            "budget_form": budget_form,
            "avancement_projet_form": avancement_projet_form,

        },
    )
