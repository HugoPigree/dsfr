from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('medical/', views.medical, name='medical'),
    path('rh/', views.rh, name='rh'),
    path('autres/', views.autres, name='autres'),
    path('drhfs/', views.drhfs, name='drhfs'),
    path('utilisateurs/', views.utilisateurs, name='utilisateurs'),
]
