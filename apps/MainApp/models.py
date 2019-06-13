from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from time import strftime
from django import forms
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def RegValidation(self, postData):
        errors = {}

        if len(postData['FirstName']) < 1:
            errors['FirstName'] = "FIRST NAME cannot be BLANK!"
        elif len(postData['FirstName']) < 2:
            errors['FirstName'] = "FIRST NAME must contain at least 2 letters MINIMUM!"
        elif not postData['FirstName'].isalpha():
            errors['FirstName'] = "FIRST NAME must contain letter's ONLY!"

        if len(postData['LastName']) < 1:
            errors['LastName'] = "LAST NAME cannot be blank!"
        elif len(postData['LastName']) < 2:
            errors['LastName'] = "LAST NAME must contain at least 2 letters MINIMUM!" 
        elif not postData['LastName'].isalpha():
            errors['LastName'] = "LAST NAME must contain letter's ONLY"

        if User.objects.filter(Email = postData['Email']):
            errors['EmailExists'] = "An account has already been created with this EMAIL!"
        if EMAIL_REGEX.match(postData['Email']) == None:
            errors['EmailFormat'] = "Invalid EMAIL FORMAT!"
        elif len(postData['Email']) < 1:
            errors['Email'] = "EMAIL cannot be BLANK!"

        if len(postData['State']) < 1:
            errors['State'] = "You must select a STATE!"

        if len(postData['City']) < 1:
            errors['City'] = "You must select a City!"

        if len(postData['ZipCode']) < 1:
            errors['ZipCode'] = "You must enter your ZIP CODE!"
        if len(postData['ZipCode']) != 5:
            errors['ZipCode'] = "You must enter a valid ZIP CODE!" 

        if len(postData['Password']) < 1:
            errors['Password'] = "PASSWORD cannot be BLANK!"
        elif len(postData['Password']) < 6:
            errors['PasswordLength'] = "PASSWORD must be at least 6 characters MINIMUM!"

        if postData['Password'] != postData['ConfirmPassword']:
            errors['ConfirmPassword'] = "PASSWORDS do not MATCH!"

        return errors

    def LoginValidation(self, postData):
        user = User.objects.filter(Email = postData['LoginEmail'])
        errors = {}
        if not user:
            errors['Email'] = "Invalid EMAIL or PASSWORD!"

        if user and not bcrypt.checkpw(postData['LoginPassword'].encode('utf8'), user[0].Password.encode('utf8')):
            errors['Password'] = "Invalid EMAIL or PASSWORD!"

        return errors

class EventManager(models.Manager):
    def EventValidation(self, postData):
        errors = {}

        if len(postData['Title']) < 1:
            errors['Title'] = "Title cannot be blank!"
        elif len(postData['Title']) < 6:
            errors['Title'] = "Title must contain at least 5 letters!"

        if len(postData['Description']) < 1:
            errors['Description'] = "Description cannot be blank!"
        elif len(postData['Description']) < 11:
            errors['Description'] = "Description must contain at least 10 letters!"

        if len(postData['EventDate']) < 1:
            errors['EventDate'] = "Event date cannot be blank!"

        if len(postData['EventTime']) < 1:
            errors['EventTime'] = "Event time cannot be blank!"

        if len(postData['Address']) < 1:
            errors['Address'] = "Address cannot be blank!"

        if len(postData['City']) < 1:
            errors['City'] = "City cannot be blank!"

        if len(postData['State']) < 1:
            errors['State'] = "State cannot be blank!"

        if len(postData['ZipCode']) < 1:
            errors['ZipCode'] = "Zip code cannot be blank!"

        return errors

    # def UpdateValidaton(self, postData):
    #     errors = {}
    #     return errors

class User(models.Model): 
    FirstName = models.CharField(max_length = 20) 
    LastName = models.CharField(max_length = 20)
    Email = models.CharField(max_length = 255)
    State = models.CharField(max_length = 2)
    City = models.CharField(max_length = 20)
    ZipCode = models.CharField(max_length = 5)
    Password = models.CharField(max_length = 255, default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Event(models.Model):
    UsersGoing = models.ManyToManyField(User, related_name = "UsersGoingRelated")
    Title = models.CharField(max_length = 255)
    Description = models.CharField(max_length = 255)
    EventDate = models.CharField(max_length = 255)
    EventTime = models.TimeField(null=True, blank=True)
    Address = models.CharField(max_length = 255)
    City = models.CharField(max_length = 20)
    State = models.CharField(max_length = 3)
    ZipCode = models.CharField(max_length = 6)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    EventByUser = models.ForeignKey(User, related_name = "EventsByUser")
    objects = EventManager()

# class EventComment(models.Model):
#     Comment = models.CharField(max_length = 255)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     Event = models.ForeignKey(Event, related_name = "Comments")
#     CommentByUser = models.ForeignKey(User, related_name = "CommentsByUser")







