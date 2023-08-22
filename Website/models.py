from django.db import models


class Employee(models.Model):
    Name = models.CharField(max_length=40)
    Salary = models.DecimalField(decimal_places=4, max_digits=10)