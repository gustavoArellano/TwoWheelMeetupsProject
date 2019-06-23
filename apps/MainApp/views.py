from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.contrib.messages import get_messages 
from .models import User
from .models import Event
from django import template
import datetime
register = template.Library()
from time import strftime
import bcrypt
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.db.models import Q


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
    AllEvents = Event.objects.all()
    AllUsers = User.objects.all()
    ThisUser = User.objects.get(id = request.session['LoggedIn'])
    UserAttending = ThisUser.UsersGoingRelated.all()
    EventsNotAttending = Event.objects.exclude(UsersGoing=ThisUser.id)
    Key = settings.API_KEY
    print(Key)
    context = {
        'users': AllUsers,
        'events': AllEvents,
        'UserLoggedIn': User.objects.get(id = request.session['LoggedIn']),
        'UserAttending': UserAttending,
        'EventsNotAttending': EventsNotAttending,
        'myKey': Key
        }
    return render(request, "MainApp/home.html", context) 

def UserProfile(request, id):
    if request.method == "POST":
        ThisUser = User.objects.get(id = request.POST['Rider'])
        UserAttending = ThisUser.UsersGoingRelated.all()
        DateJoined = ThisUser.created_at
        FormatedDate = DateJoined.strftime("%B %Y")

        context = {
            'UserAttending': UserAttending,
            'rider': ThisUser,
            'date': FormatedDate
        }
    
        return render(request, "MainApp/profile.html", context)

def CreateEvent(request):
    UserLoggedIn = User.objects.get(id = request.session['LoggedIn'])

    context = {
        'UserLoggedIn': UserLoggedIn
        }
    return render(request, "MainApp/create.html", context)

def CreateEventProcess(request):
    errors = Event.objects.EventValidation(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)
    else: 

        ThisUser = User.objects.get(id = request.session['LoggedIn'])

        Create = Event.objects.create(
            EventByUser = ThisUser,
            Title = request.POST['Title'],
            Description = request.POST['Description'],
            EventDate = request.POST['EventDate'],
            EventTime = request.POST['EventTime'],
            Address = request.POST['Address'],
            City = request.POST['City'],
            State = request.POST['State'],
            ZipCode = request.POST['ZipCode']
        )
        Create.UsersGoing.add(ThisUser)

        return redirect('/Home')
    return redirect('/CreateEvent')

def Join(request, id):
    if request.method == "POST":
        user = User.objects.get(id = request.session['LoggedIn'])
        event = Event.objects.get(id=id)
        event.UsersGoing.add(user)
        return redirect ("/Home")
    else:
        request.session.clear()
        return redirect ("/Index")

def RemoveUserFromEvent(request, id):
    if request.method == "POST":
        ThisEvent = Event.objects.get(id=id)
        ThisUser = User.objects.get(id = request.session['LoggedIn'])
        ThisEvent.UsersGoing.remove(ThisUser)   
        return redirect('/Home')

def EventDetails(request, id):
    if request.method == "POST":
        ThisEvent = Event.objects.get(id = request.POST['EventDetail'])  
        Key = settings.API_KEY
        
        context = {
            'Event': ThisEvent,
            'myKey': Key
        }
        print(context)
        return render(request, 'MainApp/eventDetail.html', context)

def Explore(request):
    UserLoggedIn = User.objects.get(id = request.session['LoggedIn'])

    context = {
        'UserLoggedIn': UserLoggedIn
        }
        
    return render(request, "MainApp/explore.html", context)

def ExploreApi(request):
    events = Event.objects.filter(
        Q(ZipCode__startswith = request.POST['StartsWith']) |
        Q(City__startswith = request.POST['StartsWith']) |
        Q(State__startswith = request.POST['StartsWith'])
    )

    context = {
        'events': events
    }
    return render(request, "MainApp/exploreApi.html", context)