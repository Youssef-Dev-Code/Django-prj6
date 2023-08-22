from django.shortcuts import render
from django.http import request, response
from .models import *
def Index(request):
    Emp = Employee()
    Emp.Name = "Youssef"
    Emp.Salary = 123456.5555
    return render(request=request, template_name="index.html", context={"Emp": Emp})
    
