from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages import get_messages 
from .models import User
import datetime
from time import strftime
import bcrypt
from django.contrib.auth import authenticate, login

def Index(request):
    return render(request, "MainApp/index.html")

def RegistrationPage(request):
    return render(request, "MainApp/register.html")

def RegistrationProcess(request):
    errors = User.objects.RegValidation(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)
    else:
        hash_pw = bcrypt.hashpw(request.POST['Password'].encode(), bcrypt.gensalt())
        User.objects.create(
            FirstName = request.POST['FirstName'], 
            LastName = request.POST['LastName'], 
            Email = request.POST['Email'], 
            State = request.POST['State'],
            City = request.POST['City'],
            ZipCode = request.POST['ZipCode'],
            Password = hash_pw
            )
        user = User.objects.last() 
        user = User.objects.get(Email = request.POST['LoginEmail'])
        request.session['LoggedIn'] = user.id
        request.session['FirstName'] = user.FirstName
        request.session['LastName'] = user.LastName
        return redirect('/Home')
    return redirect('/Register')

def LoginPage(request):
    return render(request, "MainApp/login.html")

def LoginProcess(request):
    errors = User.objects.LoginValidation(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)
    else:
        user = User.objects.get(Email = request.POST['LoginEmail'])
        request.session['LoggedIn'] = user.id
        request.session['FirstName'] = user.FirstName
        request.session['LastName'] = user.LastName
        return redirect('/Home')
    return redirect('/Login')

def Logout(request):
    request.session.clear()
    return redirect('/')

def Home(request):  
    # if request.session.['LoggedIn']:
    context = {
        'users': User.objects.all(),
        'UserLoggedIn': User.objects.get(id = request.session['LoggedIn'])
        }
    return render(request, "MainApp/home.html", context) 

def UserProfile(request, id):
    if request.method == "POST":
        ThisUser = User.objects.get(id = request.POST['Rider'])

        context = {
            'rider': ThisUser
        }
    
        return render(request, "MainApp/profile.html", context)