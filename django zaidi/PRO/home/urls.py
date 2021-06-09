from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    
    path("",views.index1, name='Home'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('contact',views.contact, name='contact'),
    path('servies',views.servies, name='servies'),
    path('Graph',views.Graph, name='Graph'),
    path('vis',views.vis, name='vis'),
    path('prediction',views.prediction, name='prediction'),
  
 ]