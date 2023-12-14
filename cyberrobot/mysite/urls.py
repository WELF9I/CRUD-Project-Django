
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('etudiants/', views.liste_etudiants, name='liste_etudiants'),
    path('articles/', views.liste_articles, name='liste_articles'),
    path('ajouter_etudiant/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('modifier_etudiant/<int:etudiant_id>/', views.modifier_etudiant, name='modifier_etudiant'),
    path('supprimer_etudiant/<int:etudiant_id>/', views.supprimer_etudiant, name='supprimer_etudiant'),
    path('articles/', views.liste_articles, name='liste_articles'),
    path('ajouter_article/', views.ajouter_article, name='ajouter_article'),
    path('modifier_article/<int:article_id>/', views.modifier_article, name='modifier_article'),
    path('supprimer_article/<int:article_id>/', views.supprimer_article, name='supprimer_article'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
