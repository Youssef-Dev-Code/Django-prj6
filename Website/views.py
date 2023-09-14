from django.shortcuts import render
from django.http import HttpResponseRedirect, request, response
from .models import *
from django.contrib import messages
import seaborn as sns
import matplotlib.pyplot as plt
import datetime, os, csv

Search_Input = ""
path_Data = os.path.join(os.getcwd(), "Data")#data directory
path_y_f = os.path.join(path_Data, "year")
with open(file = path_y_f, mode = "r") as f: # importing year val in year file
    Year = int(f.readline())
    f.close()
path_Year = os.path.join(path_Data, "{0}".format(Year))#year directory
Months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]

def Index_VIEW(request):
    if datetime.datetime.today().year == Year and os.path.isdir(path_Year) == False: #condition to create dirs only one time and change year val in year file
        with open(file = path_y_f, mode = "w") as f: # writing in year file new year val
            f.write("{0}".format(Year+1))
            f.close()
        os.system("mkdir {0}".format(path_Year))
        for month in Months:
            path_Month = os.path.join(path_Year, month)#month directory
            os.system("mkdir {0}".format(path_Month))
            os.system("touch {0}".format(os.path.join(path_Month, "Absences.csv")))
            os.system("touch {0}".format(os.path.join(path_Month, "Salaires.csv")))
    emp_list = Employé.objects.all()
    global Search_Input
    Search_Input = ""
    return render(request=request, template_name="index.html", context={"emp_list": emp_list})
    
def Affectations_VIEW(request):
    emp_list0 = Employé.objects.all()
    emp_list = list()
    global Search_Input
    for emp in emp_list0:
        if (Search_Input in emp.Prénom or Search_Input in emp.Nom or Search_Input == str(emp.id) or Search_Input == str(emp.Matricule)):
            emp_list.append(emp)
    return render(request=request, template_name="Affectations.html", context={"emp_list": emp_list})

def Banque_VIEW(request):
    emp_list0 = Employé.objects.all()
    emp_list = list()
    global Search_Input
    for emp in emp_list0:
        if (Search_Input in emp.Prénom or Search_Input in emp.Nom or Search_Input == str(emp.id) or Search_Input == str(emp.Matricule)):
            emp_list.append(emp)
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
    con = dict()
    con["Year"] = Year-1#adding year to use in template
    if request.method == "POST":
        Id = request.POST.get('Absence_Individuelle')#getting id from template of employee to get absence details
        for emp in emp_list:
            if str(emp.id) == Id:
                con["emp"] = emp #adding name to use in template
        #check in witch month we are
        int_month_Now = datetime.datetime.today().month #int month
        i = 0
        for month in Months:
            if i == int_month_Now - 1:
                str_month_Now = Months[i] #month in letters
                break
            i += 1
        path_year_now = os.path.join(path_Data, "{0}".format(datetime.datetime.today().year)) #path of this year
        i = 0
        for month in Months:
            path_Month = os.path.join(path_year_now, "{0}".format(month))#Month directory
            path_Absences = os.path.join(path_Month, "{0}".format("Absences.csv"))#Absence directory
            with open(file = path_Absences, mode = "r") as f: # lecture des absences de chaque emp dans le fichier
                csvreader = csv.reader(f)
                for row in csvreader:#HANDLE ERRORS IN THIS SECTION
                    if row[0] == Id:
                        x = 1
                        z = i
                        while x < 5:
                            con["item"+str(z+1)] = row[x]
                            print("ok")
                            x += 1
                            z += 1
                i += 4
                f.close()
        return render(request=request, template_name="Absence.html", context=con)
    else:
        return HttpResponseRedirect(redirect_to="/Absences")