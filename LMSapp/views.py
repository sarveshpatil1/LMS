from django.shortcuts import render, redirect

# Create your views here.

def BASE(request):
    return render(request,'base.html')