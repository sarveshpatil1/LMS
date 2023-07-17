from . import views, user_login
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('base', views.BASE, name='BASE'),
    path('', views.home, name='home'),
    path('singlecourse', views.singlecourse, name='singlecourse'),
    path('contactus', views.contactus, name='contactus'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', user_login.register, name='register'),

]
