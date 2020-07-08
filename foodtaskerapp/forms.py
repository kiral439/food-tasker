from django import forms

from django.contrib.auth.models import User
from foodtaskerapp.models import Restaurant

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "phone", "address", "logo")




# vue.js - frontend
    # form elements
    # http://localhost/api/v1/sign-up   /POST - data/ -> backend
    # status(200, 400) -> 200 - registered successfully...  -   400 - echo message

# android app
    # http://localhost/api/v1/sign-up   /POST - data/ -> backend

# django - backend
    # receive - http://localhost/api/v1/sign-up   /POST - data/  -> db, status(400, message) -> frontend

#db - postgresql

