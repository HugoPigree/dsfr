from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Page d'accueil
    path('ajouter-projet/', views.ajouter_projet, name='ajouter_projet'),  # Page pour ajouter un projet
    path('<str:categorie_slug>/', views.categorie_detail, name='categories_projets'),
    path('<str:categorie_slug>/<str:projet_slug>/', views.projet_detail, name='projet_detail'),
    path('<str:categorie_slug>/<str:projet_slug>/info/', views.info_projet, name='info_projet'),
]
