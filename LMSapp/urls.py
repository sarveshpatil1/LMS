from . import views, user_login
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('base', views.BASE, name='BASE'),
                  path('', views.home, name='home'),
                  path('singlecourse', views.singlecourse, name='singlecourse'),
                  path('contactus', views.contactus, name='contactus'),
                  path('aboutus', views.aboutus, name='aboutus'),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/register', user_login.REGISTER, name='register'),
                  path('accounts/doLogin', user_login.DO_LOGIN, name='doLogin'),
                  path('accounts/profile', user_login.PROFILE, name='profile'),
                  path('accounts/profile_update', user_login.Profile_Update, name='profileUpdate'),
                  path('admin/', admin.site.urls)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
