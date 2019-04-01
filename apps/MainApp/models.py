from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from time import strftime
from django import forms
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    
class User(models.Model): 
    FirstName = models.CharField(max_length = 20) 
    LastName = models.CharField(max_length = 20)
    Email = models.CharField(max_length = 255)
    City = models.CharField(max_length = 20)
    State = models.CharField(max_length = 3)
    ZipCode = models.CharField(max_length = 6)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # objects = UserManager()

class Event(models.Model):
    Title = models.CharField(max_length = 255)
    Description = models.CharField(max_length = 255)
    EventDate = models.CharField(max_length = 255)
    Address = models.CharField(max_length = 255)
    City = models.CharField(max_length = 20)
    State = models.CharField(max_length = 3)
    ZipCode = models.CharField(max_length = 6)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    CreatedByUser = models.ForeignKey(User, related_name = "CreatedByUser")
    # objects = UserManager()

class EventComment(models.Model):
    Comment = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    Event = models.ForeignKey(Event, related_name = "Comments")
    PostedByUser = models.ForeignKey(User, related_name = "PostedByUser")

class EventAttendant(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    Event = models.ForeignKey(User, related_name = "UsersGoing")






