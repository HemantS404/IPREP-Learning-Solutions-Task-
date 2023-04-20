from django.urls import path

from main import views

app_name = 'api'

urlpatterns = [
    path('', views.companies_view),
    path('employees/<id>', views.employee_view, name = 'employees'),
    path('add-employees/<id>', views.add_employee_view, name = 'add-employees'),
]
