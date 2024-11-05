from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments, Doctors

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def contact(request):
    return render(request, 'contact.html')

def deparment(request):
    dict_dep = {
        'dept' : Departments.objects.all()
    }
    return render(request, 'dept.html', dict_dep)


def doctors(request):
    dict_doct = {
        'doctors' : Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_doct)

