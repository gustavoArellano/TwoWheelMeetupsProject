from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.contrib.messages import get_messages 
from .models import *
from django import template
import datetime
register = template.Library()
from time import strftime
import bcrypt
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Q
from django.core.files.storage import FileSystemStorage


def Index(request):
    if 'LoggedIn' in request.session:
        return redirect('/Home')

    else:

        AllEvents = Event.objects.all().order_by('EventDate')[:4]

        context = {
            'Events': AllEvents
        }

        return render(request, "MainApp/index.html", context)

def RegistrationPage(request):
    if 'LoggedIn' in request.session:
        return redirect('/Home')

    else:

        return render(request, "MainApp/register.html")

def RegistrationProcess(request):
    if 'LoggedIn' in request.session:
        return redirect('/Home')

    else:
        errors = User.objects.RegValidation(request.POST)
        if len(errors):

            for key, value in errors.items():
                messages.error(request, value, extra_tags = key)

        else:

            hash_pw = bcrypt.hashpw(request.POST['Password'].encode('utf-8'), bcrypt.gensalt())
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
    if 'LoggedIn' in request.session:
        return redirect('/Home')

    else:

        return render(request, "MainApp/login.html")

def LoginProcess(request):
    if 'LoggedIn' in request.session:
        return redirect('/Home')

    else:

        errors = User.objects.LoginValidation(request.POST)

        if len(errors):

            for key, value in errors.items():
                messages.error(request, value, extra_tags = key)

        else:

            user = User.objects.get(Email = request.POST['LoginEmail'])
            request.session['LoggedIn'] = user.id
            request.session['FirstName'] = user.FirstName
            request.session['LastName'] = user.LastName
            UserLoggedIn = user

            return redirect('/Home')

        return redirect('/Login')


def ErrorPage(request):
    return render(request, "MainApp/error.html")

def Logout(request):
    request.session.clear()

    return redirect('/')

def Home(request):  
    if 'LoggedIn' not in request.session:
        return redirect('/Error')

    else:

        ThisUser = User.objects.get(id = request.session['LoggedIn'])
        AllEvents = Event.objects.all().order_by('EventDate')
        AllUsers = User.objects.all()
        UserAttending = ThisUser.UsersGoingRelated.all().order_by('EventDate').first()
        AllUserAttending = ThisUser.UsersGoingRelated.all()
        EventsNotAttending = Event.objects.exclude(UsersGoing=ThisUser.id).order_by('EventDate', 'EventTime')
        apiKey = settings.API_KEY

        context = {
            'users': AllUsers,
            'events': AllEvents,
            'UserLoggedIn': User.objects.get(id = request.session['LoggedIn']),
            'UpcomingEvent': UserAttending,
            'EventsNotAttending': EventsNotAttending,
            'AllUserAttending': AllUserAttending,
            'myKey': apiKey
            }

        return render(request, "MainApp/home.html", context) 
    
def Rider(request, uuid):
    if 'LoggedIn' not in request.session:
        return redirect('/Error')

    else:

        ThisUser = User.objects.get(id = uuid)
        UserAttending = ThisUser.UsersGoingRelated.all().order_by('EventDate', 'EventTime')
        DateJoined = ThisUser.created_at
        FormatedDate = DateJoined.strftime("%B %Y")
        GetUser = User.objects.get(id = request.session['LoggedIn'])

        context = {
            'UserAttending': UserAttending,
            'rider': ThisUser,
            'date': FormatedDate,
            'GetUser': GetUser
        }

        return render(request, "MainApp/profile.html", context)

def EditRiderPage(request, uuid):
    if 'LoggedIn' not in request.session:
        return redirect('/Error')

    if User.objects.get(id = uuid) != User.objects.get(id = request.session['LoggedIn']):
        return redirect('/Home')

    else:

        ThisUser = User.objects.get(id = uuid)

        context = {
            'rider': ThisUser
        }

        return render(request, 'MainApp/editProfile.html', context)

def ImageUpload(request, id):
    if request.method == 'POST' and request.FILES['myImage']:
        ThisUser = request.session['LoggedIn']
        myImage = request.FILES['myImage']
        fs = FileSystemStorage()
        imageUploaded = fs.save(myImage.name, myImage)

        User.objects.filter(id = ThisUser).update(Image = imageUploaded)

        return redirect('/Rider/' + id)

def UpdateInfo(request, id):
    errors = User.objects.UserUpdateValidations(request.POST)
    if len(errors):

        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)

    CheckUser = User.objects.get(id = id)        
    if request.method == 'POST': 
        ThisUser = User.objects.get(id = request.session['LoggedIn'])
        ThisUserID = request.session['LoggedIn']

        UserValues = {
            'FirstName': request.POST['FirstName'],
            'LastName': request.POST['LastName'],
            'Email': request.POST['Email'],
            'State': request.POST['State'],
            'City': request.POST['City'],
            'ZipCode': request.POST['ZipCode'],
        }

        User.objects.filter(id = ThisUser.id).update(**UserValues)

        return redirect('/Rider/' + id)

    return redirect('/EditProfile')

def CreateEvent(request):
    if 'LoggedIn' not in request.session:
        return redirect('/Error')

    else:

        UserLoggedIn = User.objects.get(id = request.session['LoggedIn'])

        context = {
            'UserLoggedIn': UserLoggedIn
            }

        return render(request, "MainApp/create.html", context)

def CreateEventProcess(request):
    if 'LoggedIn' not in request.session:
        return redirect('/Error')

    else:

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

        return redirect ("/Home")

def RemoveUserFromEvent(request, id):
    if request.method == 'POST':
        print(id)
        ThisEvent = Event.objects.get(id = id)
        ThisUser = User.objects.get(id = request.session['LoggedIn'])
        ThisEvent.UsersGoing.remove(ThisUser)  

        return redirect('/Home')

def EventDetails(request, uuid):
    if 'LoggedIn' not in request.session:
        return redirect('/Error')

    else:

        ThisUser = User.objects.get(id = request.session['LoggedIn'])
        ThisEvent = Event.objects.get(id = uuid)
        AllEvents = Event.objects.all()
        Key = settings.API_KEY
        
        context = {
            'Event': ThisEvent,
            'ThisUser': ThisUser,
            'events': AllEvents,
            'myKey': Key,
            'UserLoggedIn': User.objects.get(id = request.session['LoggedIn'])
        }

        return render(request, 'MainApp/eventDetail.html', context)

def EditEventPage(request, uuid):
    if 'LoggedIn' not in request.session:
        return redirect('/Error')

    ThisEvent = Event.objects.get(id = uuid)
    ThisUser = User.objects.get(id = request.session['LoggedIn'])

    if ThisUser.id != ThisEvent.EventByUser.id:
        return redirect('/Home')

    else:

        context = {
            'ThisEvent': ThisEvent,
            'rider': ThisUser
        }
  
        return render(request, 'MainApp/editEvent.html', context)

def UpdateEvent(request, id):
    errors = Event.objects.EventValidation(request.POST)
    if len(errors):

        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)

    if request.method == 'POST': 
        ThisEvent = Event.objects.get(id = id)

        EventValues = {
            'Title': request.POST['Title'],
            'Description': request.POST['Description'],
            'EventDate': request.POST['EventDate'],
            'EventTime': request.POST['EventTime'],
            'Address': request.POST['Address'],
            'City': request.POST['City'],
            'State': request.POST['State'],
            'ZipCode': request.POST['ZipCode']
        }

        Event.objects.filter(id = ThisEvent.id).update(**EventValues)

        return redirect('/Event/' + id)

    return redirect('/EditEvent/' + id)

def DeleteEvent(request, id):
    if request.method == "POST":
        ThisEvent = Event.objects.get(id = request.POST['Event'])
        ThisEvent.delete()

        return redirect('/Home')

def Explore(request):
    if 'LoggedIn' not in request.session:
        return redirect('/Error')

    else:

        UserLoggedIn = User.objects.get(id = request.session['LoggedIn'])

        context = {
            'UserLoggedIn': UserLoggedIn
            }
            
        return render(request, "MainApp/explore.html", context)

def ExploreApi(request):
    if 'LoggedIn' not in request.session:
        return redirect('/Home')

    else:

        events = Event.objects.filter(
            Q(ZipCode__startswith = request.POST['StartsWith']) |
            Q(City__startswith = request.POST['StartsWith']) |
            Q(State__startswith = request.POST['StartsWith'])
        )

        context = {
            'events': events
        }

        return render(request, "MainApp/exploreApi.html", context)

