
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm




def home(request):
    people = [
        {'name' : 'Loki',  'location': 'azguard'},
        {'name' : 'Thor', 'location': 'Newyork'},
        {'name' : 'Steve', 'location': 'Afganistan'}
    ]

 
    return render(request, 'home.html', context = {'people': people })

def about(request): 
    return render(request, 'about.html')

def contact(request): 
    return render(request, 'contact.html')
