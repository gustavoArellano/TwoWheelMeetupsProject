from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "MainApp/index.html")
