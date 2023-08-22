from django.shortcuts import render
from django.http import request, response
from .models import *
def Index(request):
    Emp = Employé()
    Emp.Prénom = "Youssef"
    Emp.Salaire_de_Base = 23456.5555
    return render(request=request, template_name="index.html", context={"Emp": Emp})
    
