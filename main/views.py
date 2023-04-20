from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import Company, Employee

# Create your views here.


def companies_view(request):
    company_details = Company.details()
    return render(request, 'companies.html', {'companies':company_details})

def employee_view(request,id):
    employees = Employee.unemployeed()
    return render(request, 'employees.html',{'id':id,'employees':employees})

def add_employee_view(request,id):
    employee_id = request.POST.get('employee').split(' ')[0]
    employee_obj = Employee.objects.get(id = employee_id)
    employee_obj.company = Company.objects.get(id = id)
    employee_obj.save()
    return redirect('/')