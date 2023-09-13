from django.urls import path
from .views import *
urlpatterns = [
    path(route='', view= Index_VIEW),
    path(route='Banque', view= Banque_VIEW),
    path(route='CNSS', view= CNSS_VIEW),
    path(route='Situation', view= Situation_View),
    path(route='Affectation', view= Affectations_VIEW),
    path(route='Search', view= Search_VIEW, name='Search-Employé'),
    path(route='Absences', view= Absences_VIEW),
    path(route='Absence/', view= Absence_VIEW, name='Search-Absence'),
]