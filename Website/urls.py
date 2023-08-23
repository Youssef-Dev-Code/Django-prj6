from django.urls import path
from .views import *
urlpatterns = [
    path(route='index/', view= Index_VIEW),
    path(route='index/Banque', view= Banque_VIEW),
    path(route='index/CNSS', view= CNSS_VIEW),
    path(route='index/Situation', view= Situation_View),
    path(route='index/Affectation', view= Affectations_VIEW),
]