from django.shortcuts import render
from django.http import HttpResponseRedirect, request, response
from .models import *
from django.contrib import messages
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

Search_Input = ""
  
def Index_VIEW(request):

    emp_list = Employé.objects.all()
    global Search_Input
    Search_Input = ""
    return render(request=request, template_name="index.html", context={"emp_list": emp_list})
    
def Affectations_VIEW(request):
    emp_list0 = Employé.objects.all()
    emp_list = list()
    global Search_Input
    i = 0;
    for emp in emp_list0:
        if (Search_Input in emp.Prénom or Search_Input in emp.Nom or Search_Input == str(emp.id) or Search_Input == str(emp.Matricule)):
            emp_list.append(emp)
        i += 1
    return render(request=request, template_name="Affectations.html", context={"emp_list": emp_list})

def Banque_VIEW(request):
    emp_list0 = Employé.objects.all()
    emp_list = list()
    global Search_Input
    i = 0;
    for emp in emp_list0:
        if (Search_Input in emp.Prénom or Search_Input in emp.Nom or Search_Input == str(emp.id) or Search_Input == str(emp.Matricule)):
            emp_list.append(emp)
        i += 1
    return render(request=request, template_name="Banques.html", context={"emp_list": emp_list})

def CNSS_VIEW(request):
    emp_list0 = Employé.objects.all()
    emp_list = list()
    global Search_Input
    i = 0;
    for emp in emp_list0:
        if (Search_Input in emp.Prénom or Search_Input in emp.Nom or Search_Input == str(emp.id) or Search_Input == str(emp.Matricule)):
            emp_list.append(emp)
        i += 1
    return render(request=request, template_name="CNSS.html", context={"emp_list": emp_list})

def Situation_View(request):
    emp_list0 = Employé.objects.all()
    emp_list = list()
    global Search_Input
    i = 0;
    for emp in emp_list0:
        if (Search_Input in emp.Prénom or Search_Input in emp.Nom or Search_Input == str(emp.id) or Search_Input == str(emp.Matricule)):
            emp_list.append(emp)
        i += 1
    return render(request=request, template_name="Situation.html", context={"emp_list": emp_list})

def Search_VIEW(request):
    emp_list0 = Employé.objects.all()
    emp_list = list()
    if request.method == "POST":
        global Search_Input
        Search_Input = request.POST.get('Search-Input')
        i = 0;
        cntr = 0
        if Search_Input == "": # if input is empty
            return HttpResponseRedirect(redirect_to="/")
        for emp in emp_list0:
            if (Search_Input in emp.Prénom or Search_Input in emp.Nom or Search_Input == str(emp.id) or Search_Input == str(emp.Matricule)):
                emp_list.append(emp)
                cntr += 1
            i += 1
        if cntr == 0: # if no results were found 
            messages.warning(request=request, message="Aucun résultat trouvé!")
            return HttpResponseRedirect(redirect_to="/")
        return render(request=request, template_name="Search.html", context={"emp_list": emp_list, 'Search_Input': Search_Input})
    else: # if user uses url directly
        return HttpResponseRedirect(redirect_to="/")

def Absences_VIEW(request):
    emp_list = Employé.objects.all()
    return render(request=request, template_name="Absences.html", context={"emp_list": emp_list})

def Absence_VIEW(request):
    emp_list = Employé.objects.all()
    if request.method == "POST":
        Id = request.POST.get('Absence_Individuelle')
        for emp in emp_list:
            if str(emp.id) == Id:
                return render(request=request, template_name="Absence.html", context={"emp": emp, "jour_travail": 26-emp.Id_Congés.Absence})
            else:
                print("Error")
                return HttpResponseRedirect(redirect_to="/Absences")
    else:
        return HttpResponseRedirect(redirect_to="/Absences")