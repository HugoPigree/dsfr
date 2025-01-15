from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Page de connexion par défaut
    path('accueil/', views.index, name='index'),  # Page d'accueil (accessible après connexion)
    path('ajouter-projet/', views.ajouter_projet, name='ajouter_projet'),  # Ajouter un projet
    path('projet/<int:projet_id>/', views.projet_detail, name='projet_detail'),  # Détails d'un projet
    path('projet/<int:projet_id>/info/', views.info_projet, name='info_projet'),  # Informations complètes sur un projet
    path('projet/<int:projet_id>/modifier/', views.modifier_projet, name='modifier_projet'),  # Modifier un projet
    path('projet/<int:pk>/supprimer/', views.supprimer_projet, name='supprimer_projet'),  # Supprimer un projet
    path('projet/<int:projet_id>/telecharger/', views.telecharger_fiche_projet, name='telecharger_fiche_projet'),  # Télécharger fiche projet en PDF
    re_path(r'^categorie/(?P<categorie_slug>[-\w]+)/$', views.categorie_detail, name='categories_projets'),  # Vue des catégories
    path("logout/", views.logout_view, name="logout"),  # Déconnexion
]

# Ajout des fichiers statiques et médias pour le développement local
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
