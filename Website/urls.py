from django.urls import path
from .views import *
urlpatterns = [
    path(route='index/', view= Index, name="HomePage")
]
