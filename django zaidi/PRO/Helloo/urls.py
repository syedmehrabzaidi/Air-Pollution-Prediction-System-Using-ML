"""Helloo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
import zlogin
from zlogin import userproject
from zlogin.userproject import urls
import home as hm

admin.site.site_header = "Air Pollution Predication System"
admin.site.site_title = "Admin Portal of Air Pollution Predication System"
admin.site.index_title = "Welcome to Air Pollution Predication System Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('zlogin.userproject.urls')),
    path('hom',include('home.urls')),
    path('aboutus',hm.views.aboutus, name='aboutus'),
    path('contact',hm.views.contact, name='contact'),
    path('servies',hm.views.servies, name='servies'),
    path('Graph',hm.views.Graph, name='Graph'),
    path('vis',hm.views.vis, name='vis'),
    path('prediction',hm.views.prediction, name='prediction'),
   
   

   
]
