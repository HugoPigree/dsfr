from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:categorie_slug>/<str:projet_slug>/info/', views.info_projet, name='info_projet'),  # Page d'info
    path('<str:categorie_slug>/<str:projet_slug>/', views.projet_detail, name='projet_detail'),  # Projet
    path('<str:categorie_slug>/', views.categorie_detail, name='categories_projets'),  # Catégorie
]

