from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('base', views.BASE,name='BASE')


]
