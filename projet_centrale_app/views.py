from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.contrib.staticfiles import finders
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import HttpResponseForbidden

from .models import (
    Projets,
    Organisation,
    PlanningPrevisionnel,
    MaturiteProjet,
    CaracteristiquesTechniques,
    Budget,
    AvancementProjet,
    Categorie,
    Users,
    UserSessions,
)
from .forms import (
    ProjetForm,
    OrganisationForm,
    PlanningForm,
    MaturiteForm,
    CaracteristiquesForm,
    BudgetForm,
    AvancementForm,
    LoginForm
)
from django.urls import reverse
from django.contrib import messages

# Vue pour la page d'accueil
def index(request):
    categories = Categorie.objects.prefetch_related('projets').all()
    return render(request, "projet_centrale_app/index.html", {"categories": categories})

# Vue pour afficher les projets par catégorie
def categorie_detail(request, categorie_slug):
    categorie = get_object_or_404(Categorie, slug=categorie_slug)
    projets = Projets.objects.filter(categorie=categorie)
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        user = Users.objects.get(id=user_id)

    return render(
        request,
        "projet_centrale_app/categories_projets.html",
        {"categorie": categorie, "projets": projets, "user": user,},
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

# Vue pour supprimer un projet
def supprimer_projet(request, pk):
    projet = get_object_or_404(Projets, pk=pk)
    if request.method == "POST":
        projet.delete()
        messages.success(request, f"Le projet '{projet.titre}' a été supprimé avec succès.")
        return redirect('categories_projets', categorie_slug=projet.categorie.slug)
    return redirect('index')

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
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = Users.objects.get(id=user_id)
    if not user.is_admin:
        return HttpResponseForbidden("Vous n'avez pas les droits pour accéder à cette page.")
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
def modifier_projet(request, projet_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = Users.objects.get(id=user_id)
    if not user.is_admin:
        return HttpResponseForbidden("Vous n'avez pas les droits pour accéder à cette page.")

    # Récupération des objets liés au projet
    projet = get_object_or_404(Projets, id=projet_id)
    organisation = Organisation.objects.filter(projet=projet).first()
    planning = PlanningPrevisionnel.objects.filter(projet=projet).first()
    maturite = MaturiteProjet.objects.filter(projet=projet).first()
    caracteristiques = CaracteristiquesTechniques.objects.filter(projet=projet).first()
    budget = Budget.objects.filter(projet=projet).first()
    avancement_projet = AvancementProjet.objects.filter(projet=projet).first()

    if request.method == "POST":
        # Création des formulaires avec les données POST et les fichiers téléchargés
        projet_form = ProjetForm(request.POST, request.FILES, instance=projet)
        organisation_form = OrganisationForm(request.POST, instance=organisation)
        planning_form = PlanningForm(request.POST, instance=planning)
        maturite_form = MaturiteForm(request.POST, request.FILES, instance=maturite)
        caracteristiques_form = CaracteristiquesForm(request.POST, instance=caracteristiques)
        budget_form = BudgetForm(request.POST, request.FILES, instance=budget)
        avancement_projet_form = AvancementForm(request.POST, instance=avancement_projet)

        # Validation des formulaires
        if (
            projet_form.is_valid()
            and organisation_form.is_valid()
            and planning_form.is_valid()
            and maturite_form.is_valid()
            and caracteristiques_form.is_valid()
            and budget_form.is_valid()
            and avancement_projet_form.is_valid()
        ):
            # Associer explicitement le projet avant d'enregistrer
            organisation_form.instance.projet = projet
            planning_form.instance.projet = projet
            maturite_form.instance.projet = projet
            caracteristiques_form.instance.projet = projet
            budget_form.instance.projet = projet
            avancement_projet_form.instance.projet = projet

            # Sauvegarde des formulaires
            projet_form.save()
            organisation_form.save()
            planning_form.save()
            maturite_form.save()
            caracteristiques_form.save()
            budget_form.save()
            avancement_projet_form.save()

            return redirect('projet_detail', projet_id=projet.id)
    else:
        # Préremplir les formulaires avec les instances existantes
        projet_form = ProjetForm(instance=projet)
        organisation_form = OrganisationForm(instance=organisation)
        planning_form = PlanningForm(instance=planning)
        maturite_form = MaturiteForm(instance=maturite)
        caracteristiques_form = CaracteristiquesForm(instance=caracteristiques)
        budget_form = BudgetForm(instance=budget)
        avancement_projet_form = AvancementForm(instance=avancement_projet)

    return render(
        request,
        "projet_centrale_app/modifier_projet.html",
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


def telecharger_fiche_projet(request, projet_id):
    projet = get_object_or_404(Projets, id=projet_id)
    organisation = Organisation.objects.filter(projet=projet).first()
    planning = PlanningPrevisionnel.objects.filter(projet=projet).first()
    maturite = MaturiteProjet.objects.filter(projet=projet).first()
    caracteristiques = CaracteristiquesTechniques.objects.filter(projet=projet).first()
    budget = Budget.objects.filter(projet=projet).first()

    context = {
        'projet': projet,
        'organisation': organisation,
        'planning': planning,
        'maturite': maturite,
        'caracteristiques': caracteristiques,
        'budget': budget,
        'avancement_projet': AvancementProjet.objects.filter(projet=projet).first(),

    }

    template_path = 'projet_centrale_app/fiche_projet.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="fiche_projet_{projet_id}.pdf"'

    # Charger le template en HTML
    html = render_to_string(template_path, context)

    # Inclure les fichiers statiques dans xhtml2pdf
    def link_callback(uri, rel):
        if uri.startswith("http://") or uri.startswith("https://"):
            return uri
        elif uri.startswith("/static/"):
            path = finders.find(uri.replace("/static/", ""))
            if path:
                return path
        return uri

    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback
    )

    if pisa_status.err:
        return HttpResponse('Erreur dans la génération du PDF', status=500)
    return response



def login_view(request):
    if request.method == "POST":
        matricule = request.POST.get("matricule")
        password = request.POST.get("password")

        try:
            # Récupérer l'utilisateur correspondant au matricule
            user = Users.objects.get(matricule=matricule)

            # Vérification du mot de passe
            if user.password == password:
                # Si le mot de passe correspond, l'utilisateur est authentifié
                request.session['user_id'] = user.id
                return redirect('index')
            else:
                # Si le mot de passe ne correspond pas
                messages.error(request, "Matricule ou mot de passe incorrect.")
                return redirect('login')
        except Users.DoesNotExist:
            messages.error(request, "Matricule incorrect.")

    return render(request, "projet_centrale_app/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Vous êtes déconnecté.")
    return redirect("login")
