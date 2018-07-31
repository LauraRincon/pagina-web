from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,CustomUser
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'last_name', 'profession', 'institution', 'address',
                   'email', 'phone', 'purpose')
        labels = { 'name': 'Nombre', 'last_name':'Apellido', 'profession':'Profesión', 'institution':'Institución', 'address':'Dirección', 'phone':'Teléfono', 'purpose':'Propósito'}

class CustomChangeForm(UserChangeForm):
    class Meta:
        model= CustomUser
        fields = ('username', 'name', 'last_name', 'profession', 'institution', 'address',
                   'email', 'phone', 'purpose')
