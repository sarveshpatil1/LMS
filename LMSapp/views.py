from django.shortcuts import render, redirect

# Create your views here.

def BASE(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'Main/home.html')


def singlecourse(request):
    return render(request, 'Main/singlecourse.html')


def contactus(request):
    return render(request, 'Main/contactus.html')


def aboutus(request):
    return render(request, 'Main/aboutus.html')


