"""Alumini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    # Home Page (/login)
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.home, name='home'),
    url(r'^logout/$', views.userLogout, name='user-logout'),
    url(r'^register/', include('RegisterApp.urls'), name='register'),
    url(r'^login/profile$', views.profileView, name='profile'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^reset-password/$', views.resetPassword, name='reset-password')

]
