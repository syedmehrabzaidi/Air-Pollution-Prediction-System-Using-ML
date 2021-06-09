from django.contrib import admin
from django.urls import path
#from zlogin.home import views
#from Helloo.home import views as cv
import zlogin
from zlogin.home import views

urlpatterns = [
  
     path('',zlogin.home.views.index2, name="home1"),
     path('login',zlogin.home.views.loginUser, name="login"),
     path('logout',zlogin.home.views.logoutUser, name="logout"),
    # path('inti',cv.about, name="inti"),
]