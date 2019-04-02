from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages import get_messages 
from .models import User
import datetime
from time import strftime
import bcrypt

def index(request):
    return render(request, "MainApp/index.html")

def RegistrationPage(request):
    return render(request, "MainApp/register.html")



def LoginPage(request):
    return render(request, "MainApp/login.html")