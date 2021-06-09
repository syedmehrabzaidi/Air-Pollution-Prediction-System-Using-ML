from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# password for test user is Harry$$$***000
# Create your views here.
def index2(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
   
    print(request.user)    
    return render(request, 'index2.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            print(user)
            return redirect("/hom")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
            print('pass galt hai')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

   
