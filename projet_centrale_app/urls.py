from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('medical/', views.medical, name='medical'),
    path('rh/', views.rh, name='rh'),
    path('autres/', views.autres, name='autres'),
    path('drhfs/', views.drhfs, name='drhfs'),
    path('utilisateurs/', views.utilisateurs, name='utilisateurs'),
    path('medical/delta_medical/', views.delta_medical, name='delta_medical'),
    path('medical/psycho_trauma/', views.psycho_trauma, name='psycho_trauma'),
    path('medical/handicap/', views.handicap, name='handicap'),
    path('medical/pol2as/', views.pol2as, name='pol2as'),
    path('medical/gapv/', views.gapv, name='gapv'),
    path('medical/sisspo/', views.sisspo, name='sisspo'),

    path('rh/asa/', views.asa, name='asa'),
    path('rh/nomenclature/', views.nomenclature, name='nomenclature'),
    path('rh/mobipol2/', views.mobipol2, name='mobipol2'),
    path('rh/bad/', views.bad, name='bad'),
    path('rh/retraite/', views.retraite, name='retraite'),
    path('rh/pep/', views.pep, name='pep'),
    path('rh/suivi_contractuel/', views.suivi_contractuel, name='suivi_contractuel'),
    path('rh/avancement/', views.avancement, name='avancement'),
    path('rh/choix_poste/', views.choix_poste, name='choix_poste'),
]
