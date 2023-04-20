from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def details():
        value = [{'name':company.name, 'id' : company.id, 'employees' : Employee.objects.filter(company = company.id) }for company in Company.objects.all()]
        return value

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    comment = models.TextField()
    company = models.ForeignKey(Company,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def unemployeed():
        return Employee.objects.filter(company = None)
