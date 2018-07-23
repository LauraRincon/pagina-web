from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,CustomUser
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'last_name', 'profession', 'institution', 'address',
                   'email', 'phone', 'purpose')
class CustomChangeForm(UserChangeForm):
    class Meta:
        model= CustomUser
        fields = ('username', 'name', 'last_name', 'profession', 'institution', 'address',
                   'email', 'phone', 'purpose')
