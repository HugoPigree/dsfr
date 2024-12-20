from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Page d'accueil
    path('ajouter-projet/', views.ajouter_projet, name='ajouter_projet'),  # Ajouter un projet
    path('projet/<int:projet_id>/', views.projet_detail, name='projet_detail'),  # Détails d'un projet
    path('projet/<int:projet_id>/info/', views.info_projet, name='info_projet'),  # Informations complètes sur un projet
    re_path(r'^categorie/(?P<categorie_slug>[-\w]+)/$', views.categorie_detail, name='categories_projets'),  # Vue des catégories
]
