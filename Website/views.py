from django.shortcuts import render
from django.http import request, response
from .models import *
def Index_VIEW(request):
    emp_list = Employé.objects.all()
    return render(request=request, template_name="index.html", context={"emp_list": emp_list})
    
def Affectations_VIEW(request):
    emp_list = Employé.objects.all()
    return render(request=request, template_name="Affectations.html", context={"emp_list": emp_list})

def Banque_VIEW(request):
    emp_list = Employé.objects.all()
    return render(request=request, template_name="Banques.html", context={"emp_list": emp_list})

def CNSS_VIEW(request):
    emp_list = Employé.objects.all()
    return render(request=request, template_name="CNSS.html", context={"emp_list": emp_list})

def Situation_View(request):
    emp_list = Employé.objects.all()
    return render(request=request, template_name="Situation.html", context={"emp_list": emp_list})
