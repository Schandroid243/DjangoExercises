from django.urls import path

from .views import client_list, entreprise_list, creer_client, modifier_client, supprimer_client, creer_entreprise, modifier_entreprise, supprimer_entreprise, details_client

urlpatterns = [
    path('', client_list, name='client_list'),
    path('creer', creer_client, name='creer_client'),
    path('modifier/<int:id>', modifier_client, name='modifier_client'),
    path('details/<int:id>', details_client, name='details_client'),
    path('supprimer/<int:id>', supprimer_client, name='supprimer_client'),

    path('entrprises', entreprise_list, name='entreprise_list'),
    path('entreprises/creer', creer_entreprise, name='creer_entreprise'),
    path('entreprises/modifier<int:id>', modifier_entreprise, name='modifier_entreprise'),
    path('entreprises/supprimer<int:id>', supprimer_entreprise, name='supprimer_entreprise')
]