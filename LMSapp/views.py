from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def BASE(request):
    return render(request, 'base.html')


def home(request):
    categories = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status='PUBLISH').order_by('-id')
    context = {"category": categories, "course": course}
    return render(request, 'Main/home.html', context)


def singlecourse(request):
    return render(request, 'Main/singlecourse.html')


def contactus(request):
    return render(request, 'Main/contactus.html')


def aboutus(request):
    return render(request, 'Main/aboutus.html')
