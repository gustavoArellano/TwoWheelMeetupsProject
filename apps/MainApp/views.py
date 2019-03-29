from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)
