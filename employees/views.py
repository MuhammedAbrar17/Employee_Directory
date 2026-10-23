from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Employee

# Create your views here.
def employee_details(request,id):
    employee = get_object_or_404(Employee, id=id)
    print(employee)
    return render(request,'employee_details.html', {'employee': employee})

