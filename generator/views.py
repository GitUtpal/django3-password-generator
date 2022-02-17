from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    char = list('adcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    if request.GET.get('Uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        char.extend(list('@#$%^&*()!'))
    if request.GET.get('number'):
        char.extend(list('123456789'))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(char)

    return render(request, 'generator/password.html', {'password': thepassword})
