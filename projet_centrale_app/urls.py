from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Page de login
    path('', views.login_view, name='login'),

    # Route modifiée pour la déconnexion - utilise votre vue personnalisée
    path('logout/', views.logout_view, name='logout'),
    path('accounts/logout/', views.logout_view, name='logout'),  # Route alternative pour la compatibilité

    # Vos autres URLs existantes
    path('accueil/', views.index, name='index'),  # Page d'accueil (accessible après connexion)
    path('ajouter-projet/', views.ajouter_projet, name='ajouter_projet'),
    path('projet/<int:projet_id>/', views.projet_detail, name='projet_detail'),
    path('projet/<int:projet_id>/info/', views.info_projet, name='info_projet'),
    path('projet/<int:projet_id>/modifier/', views.modifier_projet, name='modifier_projet'),
    path('projet/<int:pk>/supprimer/', views.supprimer_projet, name='supprimer_projet'),
    path('projet/<int:projet_id>/telecharger/', views.telecharger_fiche_projet, name='telecharger_fiche_projet'),
    re_path(r'^categorie/(?P<categorie_slug>[-\w]+)/$', views.categorie_detail, name='categories_projets'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
